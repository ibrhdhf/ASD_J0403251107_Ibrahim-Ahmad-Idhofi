# Nama : Ibrahim Ahmad Idhofi
# NIM : J0403251107
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree

# Latihan 1 Memahami Konsep Spanning Tree

# 1. Daftar edge pada graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# 2. Contoh spanning tree yang valid (menghubungkan semua node tanpa cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# 3 & 4. Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki semua koneksi yang mungkin dan bisa mengandung cycle, 
#    sedangkan spanning tree adalah subgraph yang menghubungkan semua node tanpa cycle.
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena cycle menandakan adanya jalur redundan yang meningkatkan biaya tanpa menambah 
#    konektivitas baru; tujuannya adalah efisiensi minimum.
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya menggunakan jumlah minimum edge (n-1) untuk menghubungkan 
#    n buah node.