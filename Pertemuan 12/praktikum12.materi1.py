'''
======================================
Nama: Ibrahim Ahmad Idhofi
NIM: J0403251107
Kelas: TPL B1
======================================
'''


import heapq

# 1. Representasi Graf menggunakan Adjacency List (Dictionary)
# Key: Node asal, Value: Dictionary berisi {tetangga: bobot/jarak}
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # 2. Inisialisasi: Setel semua jarak ke tak terhingga (inf)
    # Kecuali node awal yang disetel ke 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # 3. Priority Queue (Antrean Berprioritas)
    # Menyimpan tuple (jarak_saat_ini, nama_node)
    # heapq akan selalu menempatkan angka terkecil di posisi paling depan
    pq = [(0, start)]
    
    while pq:
        # Ambil node dengan jarak terkecil dari antrean
        current_distance, current_node = heapq.heappop(pq)
        
        # Optimasi: Jika jarak yang diambil lebih besar dari jarak yang sudah dicatat, abaikan
        if current_distance > distances[current_node]:
            continue
            
        # 4. Periksa semua tetangga dari node yang sedang diproses
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 5. Relaksasi: Jika ditemukan jalur yang lebih pendek ke tetangga tersebut
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Masukkan ke antrean untuk dieksplorasi lebih lanjut
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# Eksekusi Program
hasil = dijkstra(graph, 'A')

# Cetak hasil akhir
print("Jarak terpendek dari titik A:")
for node, dist in hasil.items():
    print(f"Ke {node} : {dist}")