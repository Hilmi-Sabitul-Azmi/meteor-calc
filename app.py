from flask import Flask, render_template, request, session, redirect, url_for
from operasi_aritmatika import hitung_aritmatika
from gerbang_logika import hitung_logika
from konversi_suhu import hitung_suhu
from konversi_uang import hitung_konversi_uang
from konversi_basis import hitung_basis
from faktorial_fibonnaci import hitung_faktorial, hitung_fibonacci
from history import simpan_ke_history

app = Flask(__name__)
app.secret_key = 'kalkulator-hilmi'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/konversi')
def konversi():
    return render_template('konversi.html')

# ======= Fungsi Aritmatika =========
@app.route('/aritmatika', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST': 
        # 1. Ambil Data Input dari Form
        hitung1 = float(request.form['hitung1'])
        hitung2 = float(request.form['hitung2'])
        operasi = request.form['operasi']
        
        # 2. Panggil Modul Logika Perhitungan
        hasil, simbol, langkah = hitung_aritmatika(hitung1, hitung2, operasi)

        # 3. Simpan ke History Session/DB
        ekspresi = f"{hitung1} {simbol} {hitung2}"
        simpan_ke_history("Aritmatika", ekspresi, hasil)
        
        # 4. Opsional: Pembulatan tampilan angka desimal agar rapi di halaman utama
        if isinstance(hasil, float):
            hasil = round(hasil, 4)
                
        return render_template('aritmatika.html', hitung1=hitung1, hitung2=hitung2, hasil=hasil, simbol=simbol, langkah=langkah)
        
    return render_template('aritmatika.html', hitung1=None, hitung2=None, hasil=None, simbol='', langkah=[])
# ========= Fungsi Konversi Suhu ==========
@app.route('/suhu', methods=['GET', 'POST'])
def suhu():
    if request.method == 'POST':
        # 1. Ambil data input dari Form
        nilai = float(request.form['nilai'])
        dari = request.form['dari']
        ke = request.form['ke']

        # 2. Panggil modul logika pemrosesan suhu
        hasil, langkah = hitung_suhu(nilai, dari, ke)

        # 3. Simpan ke History Session/DB
        ekspresi = f"{nilai} {dari} --> {ke}"
        simpan_ke_history("Suhu", ekspresi, hasil)

        # 4. Bulatkan hasil akhir float agar rapi saat tampil di HTML
        if isinstance(hasil, float):
            hasil = round(hasil, 4)

        # Kirim data ke template HTML
        return render_template('suhu.html', nilai=nilai, dari=dari, ke=ke, hasil=hasil, langkah=langkah)
        
    return render_template('suhu.html', hasil=None)

@app.route('/basis', methods=['GET', 'POST'])
def basis():
    if request.method == 'POST':
        # 1. Ambil Data Input dari Form
        angka = request.form['angka'].strip()
        dari = request.form['dari']
        ke = request.form['ke']

        # 2. Panggil Modul Logika Pemrosesan Basis Bilangan
        hasil, langkah, error_msg = hitung_basis(angka, dari, ke)
        
        # 3. Simpan ke History Session/DB
        ekspresi = f"{angka} {dari} --> {ke}"
        simpan_ke_history("Basis Bilangan", ekspresi, hasil)

        # 4. Kirim hasil pemrosesan ke template HTML
        return render_template('basis.html',
                               angka=angka, dari=dari, ke=ke,
                               hasil=hasil, langkah=langkah, error_msg=error_msg)

    # Return default saat halaman pertama kali diakses lewat method GET
    return render_template('basis.html', hasil=None, langkah=None, error_msg=None)

@app.route('/uang', methods=['GET', 'POST'])
def uang():
    if request.method == 'POST':
        try:
            nilai = float(request.form['nilai'])
            dari = request.form['dari']
            ke = request.form['ke']
            
            # Panggil fungsi logika uang
            hasil, langkah, error_msg = hitung_konversi_uang(nilai, dari, ke)

            # 3. Simpan ke History Session/DB
            ekspresi = f"{nilai} {dari} --> {ke}"
            simpan_ke_history("Mata Uang", ekspresi, hasil)
            
            return render_template('uang.html', nilai=nilai, dari=dari, ke=ke, 
                                   hasil=hasil, langkah=langkah, error_msg=error_msg)
        except ValueError:
            return render_template('uang.html', error_msg="Masukkan nilai angka yang valid!")
            
    return render_template('uang.html', hasil=None, langkah=None, error_msg=None)

@app.route('/deret', methods=['GET', 'POST'])
def deret():
    hasil = None
    langkah = []
    error_msg = None
    fitur = 'faktorial'  # Default radio button yang terpilih
    angka = ''

    if request.method == 'POST':
        fitur = request.form.get('fitur')
        angka_input = request.form.get('angka')

        try:
            angka = int(angka_input)
            
            if fitur == 'faktorial':
                hasil, langkah, error_msg = hitung_faktorial(angka)
            elif fitur == 'fibonacci':
                # Untuk fibonacci, 'hasil' berupa list/deret angka
                deret_angka, langkah, error_msg = hitung_fibonacci(angka)
                if not error_msg:
                    # Gabungkan deret angka dengan koma agar rapi saat ditampilkan
                    hasil = ", ".join(map(str, deret_angka))
                    
        except ValueError:
            error_msg = "Masukkan bilangan bulat yang valid!"

        # Simpan ke History Session/DB
        ekspresi = f"{fitur} {angka}"
        simpan_ke_history(f"{fitur}", ekspresi, hasil)

        return render_template('deret.html', angka=angka, fitur=fitur,
                               hasil=hasil, langkah=langkah, error_msg=error_msg)

    return render_template('deret.html', hasil=None, langkah=None, error_msg=None, fitur=fitur)

@app.route('/logika', methods=['GET', 'POST'])
def logika():
    hasil = None
    langkah = []
    operator = 'AND' # Default pilihan awal
    input_a = '1'
    input_b = '0'

    if request.method == 'POST':
        operator = request.form.get('operator')
        input_a = request.form.get('input_a')
        input_b = request.form.get('input_b') # Akan bernilai None jika operatornya NOT
        
        # Panggil fungsi hitung logika boolean
        hasil, langkah = hitung_logika(operator, input_a, input_b)

        # 3. Simpan ke History Session/DB
        ekspresi = f"{input_a} {operator} {input_b}"
        simpan_ke_history("Logika", ekspresi, hasil)
        
        return render_template('logika.html', operator=operator, input_a=input_a, 
                               input_b=input_b, hasil=hasil, langkah=langkah)

    return render_template('logika.html', hasil=None, langkah=None, operator=operator, 
                           input_a=input_a, input_b=input_b)

@app.route('/history')
def history():
    # Ambil data dari session, jika kosong berikan list kosong []
    daftar_riwayat = session.get('history', [])
    return render_template('history.html', history=daftar_riwayat)

@app.route('/clear-history')
def clear_history():
    # Hapus data history dari session
    session.pop('history', None)
    return redirect(url_for('history'))

if __name__ == "__main__":
    app.run(debug=True)