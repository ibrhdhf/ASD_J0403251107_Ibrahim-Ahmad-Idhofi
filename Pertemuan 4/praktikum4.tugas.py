# ======================================================================
# Nama: Ibrahim Ahmad Idhofi
# NIM: J0403251107
# Kelas: TPL B1
# ======================================================================

# ======================================================================
# Tugas: Membuat Sistem Antrian Bengkel Motor
# ======================================================================

# 1. Mendefinisikan node
class Node:
    def __init__(self, nama, servis):
        self.servis = servis      #menyimpan jenis servis
        self.nama = nama    #menyimpan nama
        self.next = None    #pointer ke node berikutnya
    
# 2. Mendefinisikan queue
class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        # ketika queue kosong, maka front = rear = None
        return self.front is None
    
    # menambahkan data baru ke bagian belakang (rear)
    def enqueue(self,nama,servis):
        nodeBaru = Node(servis,nama)
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
            print('Antrian Kosong. Tidak ada pelanggan yang dilayani\n')
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
        # jika antrian kosong, print 'antrian kosong'
        if self.is_empty():
            print('Antrian saat ini kosong.\n')
            return
        print('Daftar Antrian Pelanggan (Front -> Rear): ')
        current = self.front
        no = 1
        while current is not None:
            print(f'{no}. {current.nama} - {current.servis}')
            current = current.next
            no += 1
        print()

# 3. Program Utama

def main():
    # instantiasi queue
    q = QueueBengkel()

    while True:
        print('===== Sistem Antrian Bengkel =====')
        print('1. Tambah Pelanggan')
        print('2. Layani Pelanggan')
        print('3. Lihat Antrian')
        print('4. Keluar')

        pilihan = input('Pilih menu (1-4): ').strip()
        if pilihan == '1':
            nama = input('Masukkan Nama: ').strip()
            servis = input('Masukkan jenis servis: ').strip()
            q.enqueue(nama,servis)
            print('Pelanggan berhasil ditambahkan ke antrian\n')

        elif pilihan == '2':
            dilayani = q.dequeue()
            # penyempurnaan agar tidak error ketika antrian kosong
            if dilayani is not None:
                print(f'Pelanggan dilayani: {dilayani.nama} - {dilayani.servis}\n')

        elif pilihan == '3':
            q.tampilkan()

        elif pilihan == '4':
            print('Program selesai. Terima kasih')
            break

        else:
            print('Pilihan tidak valid. Silakan coba lagi\n')

if __name__ == "__main__":
    main()