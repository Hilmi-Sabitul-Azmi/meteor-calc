def hitung_aritmatika(hitung1, hitung2, operasi):

    hasil = None
    simbol = ''
    langkah = []

    if operasi == 'tambah':
        hasil = hitung1 + hitung2
        simbol = '+'
        langkah.append("Operasi: Penjumlahan")
        langkah.append(f"Proses : {hitung1} + {hitung2}")
        langkah.append(f"Hasil  : {hasil}")

    elif operasi == 'kurang':
        hasil = hitung1 - hitung2
        simbol = '-'
        langkah.append("Operasi: Pengurangan")
        langkah.append(f"Proses : {hitung1} - {hitung2}")
        langkah.append(f"Hasil  : {hasil}")

    elif operasi == 'kali':
        hasil = hitung1 * hitung2
        simbol = 'x'
        langkah.append("Operasi: Perkalian")
        langkah.append(f"Proses : {hitung1} × {hitung2}")
        langkah.append(f"Hasil  : {hasil}")

    elif operasi == 'bagi':
        simbol = ':'
        langkah.append("Operasi: Pembagian")
        if hitung2 != 0:
            hasil = hitung1 / hitung2
            langkah.append(f"Proses : {hitung1} ÷ {hitung2}")
            langkah.append(f"Hasil  : {hasil}")
        else:
            hasil = "Error"
            langkah.append(f"Proses : {hitung1} ÷ 0")
            langkah.append("Alasan : Dalam matematika, pembagian dengan angka nol tidak terdefinisi.")

    elif operasi == 'pangkat':
        hasil = hitung1 ** hitung2
        simbol = '^'
        langkah.append("Operasi: Perpangkatan")
        langkah.append(f"Proses : {hitung1} pangkat {hitung2}")
        langkah.append(f"Artinya: Kalikan angka {hitung1} sebanyak {hitung2} kali")
        langkah.append(f"Hasil  : {hasil}")

    elif operasi == 'akar':
        simbol = '√'
        langkah.append(f"Operasi: Akar Pangkat n (Akar {hitung2} dari {hitung1})")
        if hitung1 < 0 and hitung2 % 2 == 0:
            hasil = "Error"
            langkah.append("Alasan : Tidak bisa mencari akar pangkat genap dari bilangan negatif (menghasilkan angka imajiner).")
        else:
            hasil = round(hitung1 ** (1/hitung2), 4)
            langkah.append(f"Rumus  : {hitung1} ^ (1/{hitung2})")
            langkah.append(f"Proses : Mencari angka yang jika dipangkatkan {hitung2} hasilnya {hitung1}")
            langkah.append(f"Hasil  : {hasil} (Dibulatkan)")

    elif operasi == 'modulus':
        hasil = hitung1 % hitung2 if hitung2 != 0 else "Error"
        simbol = '%'
        langkah.append("Operasi: Modulus (Sisa Hasil Bagi)")
        if hitung2 != 0:
            pembagian_bulat = hitung1 // hitung2
            sisa = hitung1 - (pembagian_bulat * hitung2)
            langkah.append(f"Proses : {hitung1} ÷ {hitung2} = {pembagian_bulat} dengan sisa {sisa}")
            langkah.append(f"Hasil  : {hasil}")
        else:
            langkah.append("Alasan : Tidak bisa mencari sisa bagi dari nol.")

    elif operasi == 'floordiv':
        hasil = hitung1 // hitung2 if hitung2 != 0 else "Error"
        simbol = '//'
        langkah.append("Operasi: Floor Division (Pembagian Bulat Kebawah)")
        if hitung2 != 0:
            pembagian_asli = hitung1 / hitung2
            langkah.append(f"Proses : Hasil asli dari {hitung1} ÷ {hitung2} adalah {pembagian_asli}")
            langkah.append("         Dibulatkan ke bawah (dibuang desimalnya)")
            langkah.append(f"Hasil  : {hasil}")
        else:
            langkah.append("Alasan : Tidak bisa membagi pembagian bulat dengan nol.")

    return hasil, simbol, langkah