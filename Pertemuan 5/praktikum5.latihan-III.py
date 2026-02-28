# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

def cari_maks(data, index=0):
    if index == len(data) - 1:
        return data[index]
    
    maks_sisa = cari_maks(data, index + 1)
    
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# ======================================================================
# Penjelasan Latihan 3
# ======================================================================

'''
1. Alur Kode
    Program menelusuri barisan angka dari depan ke belakang terlebih dahulu hingga mencapai elemen paling akhir. Setelah itu, program berjalan mundur ke titik awal sambil membandingkan angka di posisinya dengan nilai terbesar di sebelah kanannya. Angka yang lebih besar akan terus dibawa mundur hingga menjadi hasil akhir pencarian.
2. Base Case
    Bagian ini adalah titik henti agar fungsi tidak memanggil dirinya terus-menerus. Kondisi ini tercapai saat pencarian sudah berada di elemen paling akhir dari data. Elemen terakhir tersebut langsung dikembalikan sebagai batas awal untuk mulai membandingkan.
3. Recursive Case
    Di tahap ini, fungsi memanggil dirinya sendiri untuk bergeser mengecek elemen selanjutnya (index + 1). Proses ini menunda perbandingan angka sampai program berhasil mencapai akhir data. Nilai terbesar dari sisa data di sebelah kanan kemudian disimpan sementara dalam variabel maks_sisa.
'''