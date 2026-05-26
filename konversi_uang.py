import requests

def hitung_konversi_uang(nilai, dari, ke):
    langkah = []
    hasil = None
    error_msg = None

    # Jika mata uang asal dan tujuan sama
    if dari == ke:
        hasil = nilai
        langkah.append(f"Mata uang asal dan tujuan sama ({dari}).")
        langkah.append(f"Tidak ada proses konversi.")
        return hasil, langkah, error_msg

    try:
        # Mengambil data kurs real-time dari API gratis
        url = f"https://open.er-api.com/v6/latest/{dari}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if response.status_code == 200 and data["result"] == "success":
            # Mendapatkan nilai kurs untuk mata uang tujuan
            kurs = data["rates"][ke]
            hasil = nilai * kurs
            
            # Format angka agar rapi (2 desimal di belakang koma)
            hasil = round(hasil, 2)
            kurs_formatted = f"{kurs:,.4f}" if kurs < 1 else f"{kurs:,.2f}"

            langkah.append(f"Mendapatkan kurs real-time dari API bursa.")
            langkah.append(f"Kurs Saat Ini : 1 {dari} = {kurs_formatted} {ke}")
            langkah.append(f"Rumus         : Nilai × Kurs")
            langkah.append(f"Proses        : {nilai:,} × {kurs_formatted}")
            langkah.append(f"Hasil Akhir   : {hasil:,} {ke}")
        else:
            error_msg = "Gagal mengambil data kurs terbaru dari server."

    except requests.exceptions.RequestException:
        # Antisipasi jika laptop tidak terkoneksi ke internet
        error_msg = "Koneksi internet terganggu! Gagal mengambil data kurs mata uang."

    return hasil, langkah, error_msg