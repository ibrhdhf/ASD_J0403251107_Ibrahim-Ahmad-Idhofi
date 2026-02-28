# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

def countdown(n):
    if n == 0:         
        print("Selesai")         
        return      
    print("Masuk:", n)          
    countdown(n - 1)      
    print("Keluar:", n)   

countdown(3) 

# ======================================================================
# Penjelasan Alur Latihan 1
# ======================================================================

"""
Output 'Keluar' muncul terbalik karena eksekusi fungsi rekursif bekerja menggunakan sistem memori Stack yang bersifat LIFO (Last In, First Out), artinya yang terakhir masuk antrian adalah yang pertama kali diselesaikan.
Hal ini terjadi karena baris print("Keluar:", n) diletakkan setelah pemanggilan rekursif countdown(n - 1). Akibatnya, baris tersebut tidak langsung dieksekusi, melainkan "dijeda" dan ditumpuk di dalam memori (Call Stack) sambil menunggu fungsi di bawahnya selesai.
"""