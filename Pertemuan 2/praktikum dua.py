# ===========================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# ===========================


# Latihan 1: Membuat fungsi load data
nama_file = 'data mahasiswa.txt'

def baca_data_mahasiswa(file):
    data_dict = {}
    with open(file,'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            nim,nama,nilai = baris.split(',')
            data_dict[nim] = {
                'nama': nama,
                'nilai': int(nilai)
            }
    return data_dict

# print(baca_data_mahasiswa(nama_file))
# baca_data = baca_data_mahasiswa(nama_file)


# Latihan 2: Membuat fungsi menampilkan data

def tampilkan_data(data_dict):
    # Error Handling
    if len(data_dict) == 0:
        print('Data Kosong')
        return
    
    # Header Tabel
    print('\n=== Daftar Mahasiswa ===')
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    print('-' * 33)
    
    for nim in sorted(data_dict):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {nilai: >5}")

# tampilkan_data(baca_data)

# Latihan 3: Membuat fungsi mencari data

def cari_data(data_dict):
    # mencari data berdasarkan NIM
    nim_cari = input('Masukkan NIM yang ingin dicari: ').strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print('\n=== Data Mahasiswa ===')
        print(f'NIM:   {nim_cari}')
        print(f'Nama:  {nama}')
        print(f'Nilai: {nilai}')
    else:
        print('\nData tidak ditemukan')

# cari_data(baca_data)

# Latihan 4: Membuat fungsi update nilai

def update_nilai(data_dict):
    nim = input('Masukkan NIM mahasiswa yang ingin di update: ').strip()
    if nim not in data_dict:
        print('Data tidak ditemukan')
        return
    try:
        nilai_baru = int(input('Masukkan nilai baru: ').strip())
    except ValueError:
        print('Input harus berupa angka')
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print('Input tidak masuk akal')
    nilai_lama = data_dict[nim]['nilai']
    data_dict[nim]['nilai'] = nilai_baru
    print(f'Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}')

# update_nilai(baca_data)

# Latihan 5: Membuat fungsi menyimpan perubahan data ke file

def simpan_data(nama_file, data_dict):
    with open(nama_file,'w',encoding='utf-8') as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            file.write(f'{nim},{nama},{nilai}\n')

# simpan_data(nama_file,baca_data)

# Latihan 6: Membuat Menu Program

def main():
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print('\n=== MENU DATA MAHASISWA ===')
        print('1. Tampilkan semua data')
        print('2. Mencari data')
        print('3. Update data')
        print('4. Simpan data')
        print('0. Keluar')

        pilihan = input('Pilihan menu: ').strip()
        if pilihan == '1':
            tampilkan_data(buka_data)
        elif pilihan == '2':
            cari_data(buka_data)
        elif pilihan == '3':
            update_nilai(buka_data)
        elif pilihan == '4':
            simpan_data(nama_file,buka_data)
        elif pilihan == '0':
            break
        else:
            print('Data tidak valid')

if __name__ == '__main__':
    main()