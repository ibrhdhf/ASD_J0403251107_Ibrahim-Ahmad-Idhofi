class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('null')

    def reverse_order(self):
        # deklarasi var prev untuk menunjuk ke None saat urutan sudah dibalik
        prev = None 

        # memulai dari Head
        current = self.head

        # pengulangan hingga node terakhir
        while current != None:
            next = current.next # menyimpan node selanjutnya ke var 'next' agar tidak hilang
            current.next = prev # mengubah pointer next node sekarang menjadi prev 
            prev = current # menggeser prev meju ke posisi current
            current = next # menggeser current maju ke posisi next
        
        # menukar nilai Head dan Tail
        self.tail = self.head
        self.head = prev

ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(10)
ll.insert_at_end(67)
ll.display()
ll.reverse_order()
ll.display()
