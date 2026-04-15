# ================================================
# Latihan 1 : Membuat Node
# ================================================

# class node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None #child kiri
        self.right = None #child kanan

root = Node('A')

# membuat child level 1
root.left = Node('B')
root.right = Node('C')

# membuat child level 2
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

print('Data pada root', root.data)
print('Data child kiri root', root.left.data)
print('Data child kanan root', root.right.data)
print('Data child kiri dari B', root.left.left.data)
print('Data child kanan dari B', root.left.right.data)
print('Data child kiri dari C', root.right.right.data)