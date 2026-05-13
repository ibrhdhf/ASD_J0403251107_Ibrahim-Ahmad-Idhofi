# Nama : Ibrahim Ahmad Idhofi
# NIM : J0403251107
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree

# Implementasi Kruskal untuk Kasus 2: Jaringan Komputer
edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

edges.sort() # Urutkan berdasarkan bobot

mst = []
total_weight = 0
nodes = set()
# Menggunakan set sederhana untuk simulasi konektivitas
connected_groups = [] 

def find_group(node, groups):
    for i, group in enumerate(groups):
        if node in group:
            return i
    return -1

for weight, u, v in edges:
    group_u = find_group(u, connected_groups)
    group_v = find_group(v, connected_groups)

    if group_u == -1 and group_v == -1:
        connected_groups.append({u, v})
    elif group_u != -1 and group_v == -1:
        connected_groups[group_u].add(v)
    elif group_u == -1 and group_v != -1:
        connected_groups[group_v].add(u)
    elif group_u != group_v:
        # Merge dua grup berbeda
        connected_groups[group_u].update(connected_groups[group_v])
        connected_groups.pop(group_v)
    else:
        continue # Membentuk cycle

    mst.append((u, v, weight))
    total_weight += weight

print("Hasil MST Jaringan Komputer:")
for link in mst:
    print(f"{link[0]} - {link[1]} (Bobot: {link[2]})")
print("Total Bobot Minimum:", total_weight)

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    Kasus 2: Jaringan Komputer
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal
# 3. Edge mana saja yang dipilih dalam MST?
#    RouterC-RouterD (1), RouterA-RouterC (2), RouterA-RouterB (3)
# 4. Berapa total bobot MST?
#    6
# 5. Mengapa edge tertentu tidak dipilih?
#    RouterB-RouterC (4) dan RouterB-RouterD (5) tidak dipilih karena semua router 
#    sudah terhubung melalui jalur yang lebih murah (1, 2, 3)