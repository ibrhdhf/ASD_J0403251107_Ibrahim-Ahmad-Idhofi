# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

def biner(n, hasil=''):
    if len(hasil) == n:
        print(hasil)
        return
    biner(n,hasil + '0')
    biner(n,hasil + '1')

biner(3)