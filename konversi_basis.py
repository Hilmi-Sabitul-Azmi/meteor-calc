def hitung_basis(angka, dari, ke):
 
    langkah = []  
    hasil = None
    error_msg = None

    try:
        # --- LANGKAH 1: Konversi ke decimal dulu ---
        if dari == 'decimal':
            dec = int(angka)
            langkah.append(f"Langkah 1: Angka sudah dalam bentuk Decimal = {dec}")
        elif dari == 'binary':
            dec = int(angka, 2)
            langkah.append(f"Langkah 1: Ubah Binary {angka} ke Decimal = {dec}")
        elif dari == 'octal':
            dec = int(angka, 8)
            langkah.append(f"Langkah 1: Ubah Octal {angka} ke Decimal = {dec}")
        elif dari == 'hex':
            dec = int(angka, 16)
            langkah.append(f"Langkah 1: Ubah Hex {angka} ke Decimal = {dec}")

        # --- LANGKAH 2: Konversi dari decimal ke basis tujuan ---
        if ke == 'decimal':
            hasil = str(dec)
            langkah.append(f"Langkah 2: Hasil akhir tetap Decimal = {hasil}")
        elif ke == 'binary':
            hasil = bin(dec)[2:]
            langkah.append(f"Langkah 2: Bagi {dec} dengan 2 berulang, catat sisa → {hasil}")
        elif ke == 'octal':
            hasil = oct(dec)[2:]
            langkah.append(f"Langkah 2: Bagi {dec} dengan 8 berulang, catat sisa → {hasil}")
        elif ke == 'hex':
            hasil = hex(dec)[2:].upper()
            langkah.append(f"Langkah 2: Bagi {dec} dengan 16 berulang, gunakan A–F untuk sisa → {hasil}")

    except ValueError:
        # Jika int() gagal mendeteksi angka berdasarkan basisnya
        hasil = None
        langkah = []
        error_msg = f"Angka '{angka}' tidak valid untuk sistem bilangan {dari.capitalize()}!"

    return hasil, langkah, error_msg