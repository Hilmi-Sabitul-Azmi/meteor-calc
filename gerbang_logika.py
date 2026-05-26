def hitung_logika(operator, input_a, input_b=None):
    langkah = []
    
    # Konversi string input biner ke Boolean Python
    a = True if input_a == '1' else False
    
    # Gerbang NOT hanya butuh 1 input
    if operator == 'NOT':
        hasil_bool = not a
        langkah.append(f"Operasi       : NOT {input_a}")
        langkah.append(f"Evaluasi      : Kebalikan dari {a} adalah {hasil_bool}")
    else:
        b = True if input_b == '1' else False
        langkah.append(f"Input Terbaca : A = {a} ({input_a}), B = {b} ({input_b})")
        
        if operator == 'AND':
            hasil_bool = a and b
            langkah.append(f"Aturan AND    : Hasil bernilai True (1) HANYA JIKA kedua input bernilai True (1).")
            langkah.append(f"Evaluasi      : {a} AND {b} = {hasil_bool}")
            
        elif operator == 'OR':
            hasil_bool = a or b
            langkah.append(f"Aturan OR     : Hasil bernilai True (1) JIKA SALAH SATU atau kedua input bernilai True (1).")
            langkah.append(f"Evaluasi      : {a} OR {b} = {hasil_bool}")
            
        elif operator == 'XOR':
            hasil_bool = a != b  # XOR bernilai True jika kedua input berbeda
            langkah.append(f"Aturan XOR    : Hasil bernilai True (1) JIKA kedua input MEMILIKI NILAI BERBEDA.")
            langkah.append(f"Evaluasi      : {a} XOR {b} = {hasil_bool}")
            
        elif operator == 'NAND':
            hasil_bool = not (a and b)
            langkah.append(f"Aturan NAND   : Kebalikan dari gerbang AND (NOT AND).")
            langkah.append(f"Evaluasi      : NOT ({a} AND {b}) = NOT ({a and b}) = {hasil_bool}")
            
        elif operator == 'NOR':
            hasil_bool = not (a or b)
            langkah.append(f"Aturan NOR    : Kebalikan dari gerbang OR (NOT OR).")
            langkah.append(f"Evaluasi      : NOT ({a} OR {b}) = NOT ({a or b}) = {hasil_bool}")

    # Konversi kembali dari Boolean ke simbol biner string untuk tampilan user
    hasil_biner = '1' if hasil_bool else '0'
    langkah.append(f"Hasil Akhir   : {hasil_biner} ({hasil_bool})")
    
    return hasil_biner, langkah