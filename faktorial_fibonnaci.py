def hitung_faktorial(n):
    langkah = []
    error_msg = None
    hasil = None

    if n < 0:
        error_msg = "Faktorial tidak didefinisikan untuk bilangan negatif!"
        return hasil, langkah, error_msg

    # Proses perhitungan
    hasil = 1
    proses_list = []
    
    if n == 0 or n == 1:
        proses_list.append("1")
    else:
        for i in range(n, 0, -1):
            hasil *= i
            proses_list.append(str(i))

    langkah.append(f"Rumus Faktorial: {n}! = n × (n-1) × ... × 1")
    langkah.append(f"Proses         : {' × '.join(proses_list)}")
    langkah.append(f"Hasil Akhir    : {hasil:,}")
    
    return hasil, langkah, error_msg


def hitung_fibonacci(n):
    langkah = []
    error_msg = None
    deret = []

    if n <= 0:
        error_msg = "Jumlah suku harus bilangan bulat positif (minimal 1)!"
        return deret, langkah, error_msg
    
    if n > 100:
        error_msg = "Maksimal suku yang dapat ditampilkan adalah 100 untuk menjaga performa server."
        return deret, langkah, error_msg

    # Membangun deret Fibonacci
    langkah.append("Rumus Fibonacci: F(n) = F(n-1) + F(n-2) dengan F(1)=0, F(2)=1")
    
    if n >= 1:
        deret.append(0)
        langkah.append("Suku ke-1: 0")
    if n >= 2:
        deret.append(1)
        langkah.append("Suku ke-2: 1")
        
    for i in range(2, n):
        suku_baru = deret[i-1] + deret[i-2]
        deret.append(suku_baru)
        langkah.append(f"Suku ke-{i+1}: {deret[i-1]} + {deret[i-2]} = {suku_baru}")

    return deret, langkah, error_msg