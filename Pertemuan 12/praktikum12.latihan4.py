'''
======================================
Nama: Ibrahim Ahmad Idhofi
NIM: J0403251107
Kelas: TPL B1
======================================
'''

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Menjalankan algoritma dari titik awal 'Gerbang'
hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(f"{lokasi} = {jarak} menit")

'''
==========================================================
Jawaban Analisis:
==========================================================
1. Lokasi mana yang paling dekat dari Gerbang?
   Jawaban: Kantin (dengan waktu tempuh 2 menit).

2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
   Jawaban: 7 menit. 
   Jalur: Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7 menit).

3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
   Jawaban: Tidak selalu. Sebagai contoh, jalur langsung dari Kantin ke Aula 
   memakan waktu 7 menit. Namun, jika memutar melalui Lab (Kantin -> Lab -> Aula), 
   waktu yang dibutuhkan hanya 5 menit (4 + 1). Jalur memutar bisa lebih kecil 
   jika total akumulasi bobotnya lebih rendah daripada satu edge langsung.

4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
   Jawaban: Dijkstra sangat cocok karena waktu tempuh dalam dunia nyata tidak mungkin 
   bernilai negatif (bobot positif). Selain itu, Dijkstra sangat efisien dan cepat 
   untuk menemukan rute terbaik dalam peta lokasi yang memiliki banyak titik hubung.
==========================================================
'''