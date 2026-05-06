'''
======================================
Nama: Ibrahim Ahmad Idhofi
NIM: J0403251107
Kelas: TPL B1
======================================
'''

import heapq

# 1. Representasi graph berbobot menggunakan dictionary
# Key: Kota Asal, Value: {Kota Tujuan: Waktu/Jarak}
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    # Inisialisasi jarak semua kota dengan nilai tak hingga (inf)
    distances = {node: float('inf') for node in graph}
    # Jarak ke kota asal sendiri adalah 0
    distances[start] = 0
    
    # Priority queue untuk menyimpan (jarak_akumulatif, nama_kota)
    pq = [(0, start)]
    
    while pq:
        # Mengambil kota dengan jarak terkecil dari antrean
        current_distance, current_node = heapq.heappop(pq)
        
        # Jika jarak yang diambil sudah lebih besar dari yang tercatat, lewati
        if current_distance > distances[current_node]:
            continue
            
        # Mengecek tetangga dari kota yang sedang diproses
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jalur yang lebih pendek, perbarui data distances
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Masukkan jalur baru ke dalam priority queue
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# 3. Penentuan node awal
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

# 4. Output jarak terpendek dari node awal ke semua node
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")

'''
==========================================================
Jawaban Analisis:
==========================================================
1. Node awal yang digunakan apa?
   Jawaban: Bogor.

2. Node mana yang memiliki jarak paling kecil dari node awal?
   Jawaban: Depok (jarak = 2).

3. Node mana yang memiliki jarak paling besar dari node awal?
   Jawaban: Bandung (jarak = 8).

4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
   Jawaban: 
   - Algoritma mulai dari Bogor (0). 
   - Ia melihat dua jalur: ke Jakarta (5) dan Depok (2). Ia memilih Depok karena lebih kecil.
   - Dari Depok, ia melihat jalur ke Jakarta (2+2=4) dan Bandung (2+6=8).
   - Karena jalur ke Jakarta lewat Depok (4) lebih kecil daripada jalur langsung Bogor-Jakarta (5), 
     maka jarak Jakarta diperbarui menjadi 4.
   - Terakhir, ia mengecek jalur ke Bandung. Jalur tercepat adalah lewat Depok atau Jakarta 
     (Bogor-Depok-Bandung = 8 atau Bogor-Depok-Jakarta-Bandung = 11). 
   - Algoritma menetapkan 8 sebagai jarak terpendek ke Bandung.
==========================================================
'''