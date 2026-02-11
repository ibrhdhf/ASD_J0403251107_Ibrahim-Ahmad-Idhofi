class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
    
    def display_forward(self):
        print('\nTraversing forward:')
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('null')
    
    def display_backward(self):
        print('\nTranversing backward:')
        temp = self.tail
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.prev
        print('null')

    # Method mencari node dengan Key
    def find_node(self, key):
        temp = self.head

        # Cek apakah data ada di Head
        if temp and temp.data == key:
            print(f'Elemen {key} ditemukan dalam Doubly Linked List')
            return
        
        # Looping ke elemen berikutnya jika key tidak ada di Head
        while temp and temp.data != key:
            temp = temp.next

        # Print 'tidak ditemukan' jika key tidak ada pada Linked List
        if temp is None:
            print(f'Elemen {key} tidak ditemukan')
            return
        
        # Print 'ditemukan' jika node ditemukan bukan di Head
        print(f'Elemen {key} ditemukan dalam Doubly Linked List')


dll = DoublyLinkedList()
dll.insert_at_end(3)
dll.insert_at_end(10)
dll.insert_at_end(67)
dll.insert_at_end(69)
dll.display_backward()
dll.display_forward()
dll.find_node(6)