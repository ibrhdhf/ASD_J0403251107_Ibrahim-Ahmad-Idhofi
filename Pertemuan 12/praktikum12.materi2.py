'''
======================================
Nama: Ibrahim Ahmad Idhofi
NIM: J0403251107
Kelas: TPL B1
======================================
'''

def bellman_ford(graph, start):
    # 1. Inisialisasi: Jarak ke semua node disetel tak terhingga (inf)
    # Jarak ke node awal disetel 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 2. Relaksasi Berulang (Utama)
    # Algoritma ini berjalan sebanyak (V - 1) kali, di mana V adalah jumlah node.
    # Secara teoritis, jalur terpendek tanpa siklus maksimal memiliki (V - 1) sisi.
    for _ in range(len(graph) - 1):
        # Iterasi melalui setiap node dalam graf
        for node in graph:
            # Iterasi melalui setiap tetangga dari node tersebut
            for neighbor, weight in graph[node].items():
                # Jika jarak ke 'node' sudah diketahui (bukan inf) 
                # DAN jarak baru (lewat node ini) lebih kecil dari jarak yang tercatat sebelumnya
                if distances[node] + weight < distances[neighbor]:
                    # Update jarak ke tetangga tersebut
                    distances[neighbor] = distances[node] + weight

    # Catatan: Versi ini belum menyertakan deteksi "negative cycle" (siklus negatif).
    # Biasanya ditambahkan satu iterasi lagi untuk mengecek apakah nilai masih bisa mengecil.
    
    return distances

# Contoh penggunaan:
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

hasil = bellman_ford(graph, 'A')
print(hasil)