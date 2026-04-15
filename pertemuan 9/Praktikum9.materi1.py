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

print('Data pada root', root.data)
print('Data child kiri root', root.left)
print('Data child kanan root', root.right)