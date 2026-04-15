# ================================================
# Latihan 1 : Membuat Node
# ================================================

# class node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None #child kiri
        self.right = None #child kanan

# fungsi postorder
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

# membuat tree
    # membuat root
root = Node('A')

# membuat child level 1
root.left = Node('B')
root.right = Node('C')

# membuat child level 2
root.left.left = Node('D')
root.left.right = Node('E')

print('Hasil traversal postorder')
postorder(root)
