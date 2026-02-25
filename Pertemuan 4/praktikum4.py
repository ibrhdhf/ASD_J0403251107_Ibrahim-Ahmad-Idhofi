# ==========================
# NIM: J0403251107
# Nama: Ibrahim Ahmad Idhofi
# ==========================
#=================================================
# Implementasi Dasar : Queue berbasis linked list
#=================================================

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#Queue dengan 2 pointer : front and rear
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
    #buat fungsi entry queue (enqueue)
    def is_empty(self):
        if self.front == None and self.rear == None:
            return True
        else:
            return False
    def enqueue(self,data):
        #Menamnbah data di belakang (rear)
        new_node = Node(data)
        
        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if (self.is_empty()):
            self.front = new_node
            self.rear = new_node
            return
        #Menambah node baru di belakang
        self.rear.next = new_node
        self.rear = new_node


    def dequeue(self):
        #Menghapus data dari 
        # 1) lihat data yang paling depan
        data_terhapus = self.front.data

        # 2) geser front ke node berikutnya
        self.front = self.front.next
        
        # 3) jika queue kosong
        if (self.front is None):
            #maka rear juga None
            self.rear = None
        
        return data_terhapus


    def tampilkan(self):
        current = self.front
        print("Front -> ", end="")
        while current is not None:
            print(current.data,end=" -> ")
            current = current.next
        print("None - Rear di node")

#instantiasi
qll = QueueLL()

qll.enqueue(1)
qll.enqueue(2)
qll.enqueue(3)
qll.dequeue()
qll.tampilkan()


#Membuat class node, yang merupakan calon anggota dari linked list
class Node:
    def __init__(self,data): #Membuat constructor pada linked list
        self.data = data # Menyimpan data ke dalam node
        self.next = None # Membuat Pointer 
        

#1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Menghubungkan Node
# Menghubungkan Node A -> B -> C
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None

#3) Menentukan Node Pertama
head = nodeA

#4) Traversal : Menyelusuri data pada linked list dari awal hingga akhir
current = head #Mulai dari head
while current is not None: #Selama masih ada node yang dapat diakses
    print(current.data) #cetak data saat ini
    current = current.next #beralih ke data selanjutna

#========================================================
#   Implementasi Dasar : Linked List + Insert awal
#========================================================

class LinkedList:
    def __init__(self):
        self.head = None #Awalnya Kosong

    def insert_awal(self,data): #Konsep Push pada stack
        #Daftarkan data baru sebagai node
        nodebaru = Node(data)
        #Buat node baru menunjuk ke head data yang ada
        nodebaru.next = self.head
        #Ganti head dengan data yang baru saja disambungkan ke head lama
        self.head = nodebaru

    def hapus_awal(self): #Pop dalam stack
        data_terhapus = self.head.data #Peek dalam stack
        #Menggeser head ke node selanjutnya
        self.head = self.head.next
        print("Node yang telah terhapus : ", data_terhapus)
        
    def tampilkan(self): #Implementasi traversal
        current = self.head
        while(current is not None):
            print(current.data)
            current = current.next

ll = LinkedList()
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()