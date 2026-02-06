# deklarasi variabel global
nama_file = 'stok_barang.txt'

# =======================================================
# Fungsi pembantu agar kode lebih rapi
# ======================================================

# 1. Fungsi untuk memastikan input stok adalah angka bulat nonnegatif
def input_stok(prompt):
    while True:
        angka = input(prompt).strip()
        try:
            nilai = int(angka)
            if nilai < 0:
                print('Stok tidak boleh negatif. Silakan coba lagi.')
            else:
                return nilai
        except ValueError:
            print('Input tidak valid. Masukkan angka bulat nonnegatif.')


# =======================================================
# Fungsi utama program
# =======================================================

# 1. Fungsi baca data dari file
# --------------------------------------------------

def baca_data(nama_file):
    data_dict = {}

    # membuka file
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            for baris in file:
                baris = baris.strip()
                kode,nama,stok = baris.split(',')
                data_dict[kode] = {
                    'nama': nama,
                    'stok': int(stok)
                }
    # menangani kesalahan pembacaan file
    except Exception as e:
        print('Gagal membaca file:', e) 
    return data_dict

# data_barang = baca_data(nama_file)

# 2. Fungsi tampilkan data
# --------------------------------------------------

def tampilkan_data(data_dict):
    # menampilkan header tabel
    print('\n========= Daftar Stok Barang =========')
    print(f'{"Kode":<7} | {"Nama Barang":<20} | {"Stok":<6}')
    print('-' * 39)
    # menampilkan isi tabel
    for kode in sorted(data_dict):
        nama = data_dict[kode]['nama']
        stok = data_dict[kode]['stok']
        print(f'{kode:<7} | {nama:<20} | {stok:<6}')

# tampilkan_data(data_barang)

# 3. Fungsi cari stok barang
# --------------------------------------------------

def cari_stok(data_dict):
    kode_barang = input('Masukkan kode barang yang ingin dicari: ').strip()

    # mengecek apakah kode barang ada dalam data
    if kode_barang in data_dict:
        nama = data_dict[kode_barang]['nama']
        stok = data_dict[kode_barang]['stok']

        print('\n=== Data Barang ===')
        print(f'Kode Barang   : {kode_barang:}')
        print(f'Nama Barang   : {nama}')
        print(f'Stok Sekarang : {stok}')
    else:
        print('\nBarang tidak ditemukan.')
        return

# cari_stok(data_barang)

# 4. Fungsi tambah stok barang
# --------------------------------------------------

def tambah_stok(data_dict):
    kode_barang = input('Masukkan kode barang baru: ').strip()

    # mengecek apakah kode barang sudah ada
    if kode_barang in data_dict:
        print('\nBarang sudah ada. Gunakan fitur update stok untuk mengubah stok.')
        return
    
    nama_barang = input('Masukkan nama barang: ').strip()

    stok_awal = input_stok('Masukkan stok awal: ') # menggunakan fungsi input_stok

    # menambahkan data barang baru ke dalam dictionary
    data_dict[kode_barang] = {
        'nama': nama_barang,
        'stok': stok_awal
    }
    print(f'\nBarang dengan kode {kode_barang} berhasil ditambahkan.')

# tambah_stok(data_barang)
# tampilkan_data(data_barang)

# 5. Fungsi update stok barang
# --------------------------------------------------

def update_stok(data_dict):
    kode_barang = input('Masukkan kode barang yang ingin diuppdate: ').strip()

    # mengecek apakah kode barang ada dalam data
    if kode_barang not in data_dict:
        print('\nBarang tidak ditemukan.')
        return
    
    stok_baru = input_stok('Masukkan stok baru: ') # menggunakan fungsi input_stok
    stok_lama = data_dict[kode_barang]['stok'] # menyimpan stok lama sebelum diupdate
    data_dict[kode_barang]['stok'] = stok_baru

    print(f'\nStok barang dengan kode {kode_barang} berhasil diupdate dari {stok_lama} menjadi {stok_baru}.')

# update_stok(data_barang)
# tampilkan_data(data_barang)

# 6. Fungsi simpan data kembali ke file
# --------------------------------------------------

def simpan_data(nama_file, data_dict):
    # menyimpan data ke file
    try:
        with open(nama_file, 'w', encoding='utf-8') as file:
            for kode in sorted(data_dict):
                nama = data_dict[kode]['nama']
                stok = data_dict[kode]['stok']
                file.write(f'{kode},{nama},{stok}\n')
            print('Data berhasil disimpan ke file.')
    # menangani kesalahan penyimpanan file
    except Exception as e:
        print('Gagal menyimpan data ke file:', e)

# simpan_data(nama_file, data_barang)
# tampilkan_data(data_barang)

# =======================================================
# Fungsi main untuk menjalankan program
# =======================================================

def main():
    # membaca data dari file saat program dimulai
    data_barang = baca_data(nama_file)
    while True:
        print('\n====== Menu Stok Barang ======')
        print('1. Tampilkan Data Stok Barang')
        print('2. Cari Stok Barang')
        print('3. Tambah Stok Barang')
        print('4. Update Stok Barang')
        print('5. Simpan ke file')
        print('0. Keluar')
        
        pilihan = input('Pilih menu (1-5): ').strip()
        
        if pilihan == '1':
            tampilkan_data(data_barang)
        elif pilihan == '2':
            cari_stok(data_barang)
        elif pilihan == '3':
            tambah_stok(data_barang)
        elif pilihan == '4':
            update_stok(data_barang)
        elif pilihan == '5':
            simpan_data(nama_file, data_barang)
            print('Data berhasil disimpan')
        elif pilihan == '0':
            print('Keluar dari program.')
            break
        else:
            print('Pilihan tidak valid. Silakan coba lagi.')    

if __name__ == '__main__':
    main()