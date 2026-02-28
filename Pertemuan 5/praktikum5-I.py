# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

# ======================================================================
# Materi Rekursif: Faktorial
# recursive case => 3! = 3 x 2 x 1
# base case => 0 berhenti
# ======================================================================

def faktorial(n):
    if n == 0:
        return
    # recursive case
    return n * faktorial(n-1)

print(faktorial(5))