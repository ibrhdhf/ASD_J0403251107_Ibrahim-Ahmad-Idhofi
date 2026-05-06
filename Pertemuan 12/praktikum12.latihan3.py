'''
======================================
Nama: Ibrahim Ahmad Idhofi
NIM: J0403251107
Kelas: TPL B1
======================================
'''

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================
# Weighted graph dengan bobot negatif

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

# Menjalankan algoritma
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

'''
==========================================================
Jawaban Analisis:
==========================================================
1. Berapa bobot langsung dari A ke B?
   Jawaban: Bobot langsungnya adalah 5

2. Berapa total bobot jalur A -> C -> B?
   Jawaban: Total bobotnya adalah 2

3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
   Jawaban: Jalur A -> C -> B

4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
   Jawaban: Karena Bellman-Ford tidak menggunakan pendekatan greedy. Ia melakukan 
   iterasi (relaksasi) pada seluruh sisi berkali-kali (V-1), sehingga memungkinkan 
   pembaruan jarak jika ditemukan jalur negatif yang lebih menguntungkan di tahap berikutnya.

5. Apa yang dimaksud dengan proses relaksasi edge?
   Jawaban: Proses memperbarui jarak terpendek ke sebuah node tujuan jika ditemukan 
   jalur melalui node perantara yang menghasilkan total bobot lebih kecil 
   dibandingkan jarak yang sudah tercatat sebelumnya.

6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
   Jawaban: Perbedaan utama terletak pada kemampuan menangani bobot negatif (Bellman-Ford 
   bisa, Dijkstra tidak) dan efisiensi waktu (Dijkstra jauh lebih cepat dengan 
   kompleksitas O(E log V), sedangkan Bellman-Ford lebih lambat dengan O(V * E)).
==========================================================
'''