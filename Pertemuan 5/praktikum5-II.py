# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

# ======================================================================
# Materi Rekursif: Call Stack
# tracing bilangan (masuk-keluar)
# input 3
# ======================================================================

def hitung(n):
    if n == 0:
        print('Selesai')
        return
    print('Masuk:', n)
    hitung(n-1)
    print('Keluar:',n)

hitung(5)