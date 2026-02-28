# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

# ======================================================================
# Materi Rekursif: Menjumlahkan Elemen List
# ======================================================================

def jumlah_list(data,index=0):
    if index == len(data):
        return 0
    return data[index] + jumlah_list(data, index+1)

print(jumlah_list([4,3,4,4,4,3,2,11,31,3,24]))