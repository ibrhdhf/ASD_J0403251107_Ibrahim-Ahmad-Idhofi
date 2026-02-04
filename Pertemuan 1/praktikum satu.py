# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1A: Membaca Seluruh Isi File


# Membuka File
with open('data mahasiswa.txt', 'r', encoding='UTF-8') as file:
    isi_file = file.read()
print(type(isi_file))
print(len(isi_file))
print(isi_file.count('\n')+1)


# Membuka File per Baris
jumlahBaris = 0
with open('data mahasiswa.txt', 'r', encoding='UTF-8') as file:
    for baris in file:
        jumlahBaris = jumlahBaris + 1
        baris = baris.strip()
        print('Baris ke ', jumlahBaris)
        print('Isinya: ', baris)
        print()


# Memisahkan (Parsing) baris menjadi kolom data
with open('data mahasiswa.txt', 'r', encoding='UTF-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        print(f'Nama: {nama}\nNIM: {nim}\nNilai: {nilai}\n')


# Membaca File dan Menyimpannya ke List
data_list = []
with open('data mahasiswa.txt', 'r', encoding='UTF-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        data_list.append([nama,nim,int(nilai)])
print('============== Data Mahasiswa ==============')
print(data_list)
print('============== Jumlah Record ==============')
print(len(data_list))
print('============== Menampilkan Data Record Tertentu ==============')
print(data_list[0])


# Membaca File dan Menyimpannya ke Dictionary
data_dict = {}
with open('data mahasiswa.txt', 'r', encoding='UTF-8') as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        data_dict[nim] = {          #key
            'nama': nama,           #values
            'nilai': int(nilai)     #values
        }
print(data_dict)