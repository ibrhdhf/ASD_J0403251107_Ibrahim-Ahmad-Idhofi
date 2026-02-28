# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

def buat_pin(panjang, hasil=""):      
	if len(hasil) == panjang:         
		print("PIN:", hasil)         
		return      
	for angka in ["0", "1", "2"]:         
		buat_pin(panjang, hasil + angka)   

buat_pin(3) 

# ======================================================================
# Penjelasan Latihan 4
# ======================================================================

'''
Untuk mencegah pengulangan angka yang sama, maka perlu ditambah kondisi if di dalam for dengan kode sebagai berikut:
    for angka in ['0','1','2']:
        if angka not in hasil:
            buat_pin(panjang, hasil + angka)

Kondisi if di atas bertugas sebagai penyaring karakter. Program hanya akan melakukan pemanggilan diri sendiri jika angka yang sedang diuji belum pernah dimasukkan ke dalam variabel hasil sebelumnya, sehingga output akhirnya hanya berupa kombinasi angka yang unik (seperti 012, 021, 102, dst.)
'''