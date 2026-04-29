#====================================
# Nama : Ibrahim Ahmad Idhofi
# NIM : J0403251107
# KELAS : TPL B1
#====================================

#====================================
# Latihan 1 : Study kasus BFS
#====================================

from collections import deque

graph = {
    'Rumah' : ['Sekolah', 'Toko'],
    'Sekolah' : ['Perpustakaan'],
    'Toko' : ['Pasar'],
    'Perpustakaan' : [],
    'Pasar' : []
}

def bfs(graph, start):
    visited = set() # Set untuk menyimpan node yang sudah dikunjungi
    queue = deque([start]) # Queue untuk BFS, mulai dengan node awal

    visited.add(start) # Tandai node awal sebagai sudah dikunjungi
    while queue:
        node = queue.popleft() # Ambil node dari depan queue
        print(node) # Kunjungi node
        # Tambahkan semua tetangga yang belum dikunjungi ke dalam queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor) # Tandai tetangga sebagai sudah dikunjungi
                queue.append(neighbor) # Tambahkan tetangga ke dalam queue

print("BFS Traversal of the Graph:")
bfs(graph, 'Rumah') # Memulai BFS dari node 'Rumah'

"""
Pertanyaan Analisis 
1. Node mana yang dikunjungi pertama?  
2. Mengapa BFS cocok untuk mencari jalur terdekat?  
3. Apa perbedaan urutan BFS jika struktur graph diubah? 

Jawaban Analisis
1. Node 'Rumah'. Karena 'Rumah' dipassing sebagai parameter 'start' 
   pada fungsi bfs, sehingga ia menjadi elemen pertama yang masuk ke dalam 
   antrean (queue) dan langsung diproses.

2. Karena BFS bekerja secara "level-by-level" (melebar). Algoritma ini 
   memeriksa semua node pada jarak 1 langkah sebelum pindah ke jarak 2 langkah. 
   Dengan cara ini, saat tujuan ditemukan, jalur tersebut dijamin merupakan 
   jalur terpendek karena tidak ada jalur yang lebih dekat yang terlewatkan.

3. Perubahan struktur graf akan mengubah urutan traversal secara drastis.
   - Jika urutan list tetangga diubah (misal: 'Toko' sebelum 'Sekolah'), maka 
     'Toko' dan cabangnya akan diproses lebih dulu.
   - Jika ada "shortcut" baru (misal: 'Rumah' langsung ke 'Pasar'), maka 'Pasar' 
     akan muncul lebih awal di urutan (Level 1) daripada sebelumnya (Level 2).
