from flask import session
def simpan_ke_history(kategori, ekspresi, hasil):
    # Jika belum ada list 'history' di session, buat baru
    if 'history' not in session:
        session['history'] = []
    
    # Ambil data history saat ini
    riwayat_sekarang = session['history']
    
    # Tambahkan data baru ke baris paling atas (indeks 0)
    data_baru = {
        'kategori': kategori,
        'ekspresi': ekspresi,
        'hasil': hasil
    }
    riwayat_sekarang.insert(0, data_baru)
    
    # Batasi riwayat maksimal 10 data terakhir agar memori tidak penuh
    session['history'] = riwayat_sekarang[:10]