# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

def pangkat(a, n): 
    
    # Base case 
    if n == 0: 
        return 1 
    
    # Recursive case 
    return a * pangkat(a, n - 1)

print(pangkat(2, 4))  # Output: 16 

# ======================================================================
# Penjelasan Alur Latihan 1
# ======================================================================

"""
1. Alur Program:
    Program menerima input a dan n, lalu diproses ke dalam fungsi pangkat.
    Program memanggil fungsi pangkat hingga n = 0 dengan urutan:
    a. pangkat(2, 4) memanggil 2 * pangkat(2, 3)
    b. pangkat(2, 3) memanggil 2 * pangkat(2, 2)
    c. pangkat(2, 2) memanggil 2 * pangkat(2, 1)
    d. pangkat(2, 1) memanggil 2 * pangkat(2, 0)
    e. pangkat(2, 0) mencapai base case, mengembalikan nilai 1

    Setelah base case tercapai (n = 0), nilai dikembalikan untuk dieksekusi satu per satu secara mundur
    a. pangkat(2, 1) -> 2 * 1 = 2
    a. pangkat(2, 2) -> 2 * 2 = 4
    a. pangkat(2, 4) -> 2 * 4 = 8
    a. pangkat(2, 8) -> 2 * 8 = 16

    Hasil akhir fungsi adalah 16 dan dicetak oleh print()

2. Base Case
    if n == 0: return 1
    penggalan kode tersebut adalah base case ketika n = 0 sehingga mencegah fungsi melakukan infinite loop

3. Recursice Case
    return a * pangkat(a, n-1)
    penggalan kode tersebut adalah recursive case karena selama n != 0, fungsi akan memanggil dirinya sendiri dengan n-1 setiap memanggil dirinya sendiri
"""