# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

def kombinasi(n, hasil=""):      
	if len(hasil) == n:         
		print(hasil)         
		return      
	kombinasi(n, hasil + "A")     
	kombinasi(n, hasil + "B")   

kombinasi(2) 

# ======================================================================
# Penjelasan Latihan 4
# ======================================================================

'''
Program ini membentuk pohon rekursi bercabang dua karena pada setiap langkahnya terdapat dua pilihan: menambahkan huruf "A" atau huruf "B". Secara umum, jumlah kombinasi karakter yang dihasilkan akan mengikuti rumus 2^n.
'''