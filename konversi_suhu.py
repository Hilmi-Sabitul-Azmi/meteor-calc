def hitung_suhu(nilai, dari, ke):

    hasil = None
    langkah = []

    # Jika basis asal dan tujuan sama
    if dari == ke:
        hasil = nilai
        langkah.append(f"Satuan asal dan tujuan sama ({dari.capitalize()}).")
        langkah.append("Tidak ada perubahan nilai.")
        langkah.append(f"Hasil = {nilai}")

    elif dari == 'celsius':
        if ke == 'fahrenheit':
            hasil = (nilai * 9/5) + 32
            langkah.append("Rumus: (Celsius × 9/5) + 32")
            langkah.append(f"Proses: ({nilai} × 9/5) + 32")
            langkah.append(f"        = {nilai * 9/5} + 32")
            langkah.append(f"Hasil  = {hasil}°F")
        elif ke == 'kelvin':
            hasil = nilai + 273.15
            langkah.append("Rumus: Celsius + 273.15")
            langkah.append(f"Proses: {nilai} + 273.15")
            langkah.append(f"Hasil  = {hasil} K")
        elif ke == 'reamur':
            hasil = nilai * 4/5
            langkah.append("Rumus: Celsius × 4/5")
            langkah.append(f"Proses: {nilai} × 4/5")
            langkah.append(f"Hasil  = {hasil}°R")

    elif dari == 'fahrenheit':
        if ke == 'celsius':
            hasil = (nilai - 32) * 5/9
            langkah.append("Rumus: (Fahrenheit - 32) × 5/9")
            langkah.append(f"Proses: ({nilai} - 32) × 5/9")
            langkah.append(f"        = {nilai - 32} × 5/9")
            langkah.append(f"Hasil  = {hasil}°C")
        elif ke == 'kelvin':
            hasil = (nilai - 32) * 5/9 + 273.15
            langkah.append("Rumus: ((Fahrenheit - 32) × 5/9) + 273.15")
            langkah.append(f"Proses: Ubah ke Celsius dulu -> ({nilai} - 32) × 5/9 = {(nilai - 32) * 5/9}°C")
            langkah.append(f"        Ubah ke Kelvin  -> {(nilai - 32) * 5/9} + 273.15")
            langkah.append(f"Hasil  = {hasil} K")
        elif ke == 'reamur':
            hasil = (nilai - 32) * 4/9
            langkah.append("Rumus: (Fahrenheit - 32) × 4/9")
            langkah.append(f"Proses: ({nilai} - 32) × 4/9")
            langkah.append(f"        = {nilai - 32} × 4/9")
            langkah.append(f"Hasil  = {hasil}°R")

    elif dari == 'kelvin':
        if ke == 'celsius':
            hasil = nilai - 273.15
            langkah.append("Rumus: Kelvin - 273.15")
            langkah.append(f"Proses: {nilai} - 273.15")
            langkah.append(f"Hasil  = {hasil}°C")
        elif ke == 'fahrenheit':
            hasil = (nilai - 273.15) * 9/5 + 32
            langkah.append("Rumus: ((Kelvin - 273.15) × 9/5) + 32")
            langkah.append(f"Proses: Ubah ke Celsius dulu -> {nilai} - 273.15 = {nilai - 273.15}°C")
            langkah.append(f"        Ubah ke Fahrenheit -> ({nilai - 273.15} × 9/5) + 32")
            langkah.append(f"        = {(nilai - 273.15) * 9/5} + 32")
            langkah.append(f"Hasil  = {hasil}°F")
        elif ke == 'reamur':
            hasil = (nilai - 273.15) * 4/5
            langkah.append("Rumus: (Kelvin - 273.15) × 4/5")
            langkah.append(f"Proses: Ubah ke Celsius dulu -> {nilai} - 273.15 = {nilai - 273.15}°C")
            langkah.append(f"        Ubah ke Reamur     -> {nilai - 273.15} × 4/5")
            langkah.append(f"Hasil  = {hasil}°R")

    elif dari == 'reamur':
        if ke == 'celsius':
            hasil = nilai * 5/4
            langkah.append("Rumus: Reamur × 5/4")
            langkah.append(f"Proses: {nilai} × 5/4")
            langkah.append(f"Hasil  = {hasil}°C")
        elif ke == 'fahrenheit':
            hasil = (nilai * 9/4) + 32
            langkah.append("Rumus: (Reamur × 9/4) + 32")
            langkah.append(f"Proses: ({nilai} × 9/4) + 32")
            langkah.append(f"        = {nilai * 9/4} + 32")
            langkah.append(f"Hasil  = {hasil}°F")
        elif ke == 'kelvin':
            hasil = (nilai * 5/4) + 273.15
            langkah.append("Rumus: (Reamur × 5/4) + 273.15")
            langkah.append(f"Proses: Ubah ke Celsius dulu -> {nilai} × 5/4 = {nilai * 5/4}°C")
            langkah.append(f"        Ubah ke Kelvin     -> {nilai * 5/4} + 273.15")
            langkah.append(f"Hasil  = {hasil} K")

    return hasil, langkah