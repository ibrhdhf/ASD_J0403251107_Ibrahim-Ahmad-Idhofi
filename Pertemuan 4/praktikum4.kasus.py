# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

# ======================================================================
# Studi Kasus
# Implementasi Queue
# Enqueue ==> memindahkah pointer rear
# Dequeue ==> memindahkan pointer front
# Front -> A -> B -> C -> Rear
# ======================================================================

# 1. Mendefinisikan node
class Node:
    def __init__(self, nim, nama):
        self.nim = nim      #menyimpan NIM
        self.nama = nama    #menyimpan nama
        self.next = None    #pointer ke node berikutnya
    
# 2. Mendefinisikan queue
class QueueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        # ketika queue kosong, maka front = rear = None
        return self.front is None
    
    # menambahkan data baru ke bagian belakang (rear)
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama)
        # jika data baru masuk dari queue yang kosong
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        # jika queue tidak kosong, maka data baru diletakkan setelah rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    # menghapus data paling depan (front)
    def dequeue(self):
        if self.is_empty():
            print('Antrian Kosong. Tidak ada mahasiswa yang dilayani\n')
            return None

        # lihat data bagian front, simpan di variabel data yang akan dihapus
        node_dilayani = self.front

        # geser pointer ke next front
        self.front = self.front.next

        # jika data antrian terakhir yang dilayani (front menjadi none), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani

    def tampilkan(self):
        print('Daftar Antrian Mahasiswa (Front -> Rear): ')
        current = self.front
        no = 1
        while current is not None:
            print(f'{no}. {current.nim} - {current.nama}')
            current = current.next
            no += 1
        print()

# 3. Program Utama

def main():
    # instantiasi queue
    q = QueueAkademik()

    while True:
        print('===== Sistem Antrian Akademik =====')
        print('1. Tambah Mahasiswa')
        print('2. Layani Mahasiswa')
        print('3. Lihat Antrian')
        print('4. Keluar')

        pilihan = input('Pilih menu (1-4): ').strip()
        if pilihan == '1':
            nim = input('Masukkan NIM: ').strip()
            nama = input('Masukkan nama: ').strip()
            q.enqueue(nim,nama)
            print('Mahasiswa berhasil ditambahkan ke antrian\n')

        elif pilihan == '2':
            dilayani = q.dequeue()
            print(f'Mahasiswa dilayani: {dilayani.nim} - {dilayani.nama}')

        elif pilihan == '3':
            q.tampilkan()

        elif pilihan == '4':
            print('Program selesai. Terima kasih')
            break

        else:
            print('Pilihan tidak valid. Silakan coba lagi\n')

if __name__ == "__main__":
    main()