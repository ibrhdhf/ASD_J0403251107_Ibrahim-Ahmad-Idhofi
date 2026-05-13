# Nama : Ibrahim Ahmad Idhofi
# NIM : J0403251107
# Kelas : TPL B1
# Praktikum 13 - Graph III: Spanning Tree

# Latihan 4 Studi Kasus: Jaringan Kabel Antargedung

import heapq

# Representasi weighted graph untuk jaringan gedung
gedung_graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungB': 3, 'GedungC': 1, 'GedungA': 5}
}

def hitung_mst_kabel(graph, start_node):
    visited = set([start_node])
    heap = []
    for target, weight in graph[start_node].items():
        heapq.heappush(heap, (weight, start_node, target))
    
    mst_result = []
    min_cost = 0
    
    while heap:
        weight, src, dest = heapq.heappop(heap)
        if dest not in visited:
            visited.add(dest)
            mst_result.append((src, dest, weight))
            min_cost += weight
            for nxt_dest, nxt_weight in graph[dest].items():
                if nxt_dest not in visited:
                    heapq.heappush(heap, (nxt_weight, dest, nxt_dest))
    return mst_result, min_cost

edges_pilihan, total_biaya = hitung_mst_kabel(gedung_graph, 'GedungA')

print("Jaringan Kabel Terpilih:")
for e in edges_pilihan:
    print(f"{e[0]} ke {e[1]} (Biaya: {e[2]})")
print(f"Total Biaya Minimum: {total_biaya}")

# Jawaban:
# 1. Algoritma apa yang digunakan?
#    Algoritma Prim
# 2. Edge mana saja yang dipilih?
#    (GedungA, GedungC, 2), (GedungC, GedungD, 1), dan (GedungD, GedungB, 3)
# 3. Berapa total biaya minimum?
#    6
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena tujuannya adalah menghubungkan semua titik (gedung) dengan total biaya termurah 
#    tanpa perlu jalur melingkar (cycle)