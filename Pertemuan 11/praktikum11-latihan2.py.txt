#====================================
# Nama : Ibrahim Ahmad Idhofi
# NIM : J0403251107
# KELAS : TPL B1
#====================================

#====================================
# Latihan 2 : Studi Kasus DFS
#====================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, start, visited):
    visited.add(start) # Tandai node saat ini sebagai sudah dikunjungi
    print(start, end=" ") # Kunjungi node

    for neighbor in graph[start]: # Kunjungi semua tetangga
        if neighbor not in visited:
            dfs(graph, neighbor, visited) # Rekursi untuk tetangga yang belum dikunjungi

visited = set() # Set untuk menyimpan node yang sudah dikunjungi

print("DFS Traversal of the Graph:")
dfs(graph, 'A', visited) # Memulai DFS dari node 'A'

"""
Pertanyaan Analisis 
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
2. Apa yang terjadi jika urutan neighbor diubah?  
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.

Jawaban Analisis
1. Karena DFS menggunakan mekanisme rekursi (stack) yang langsung 
   mengeksplorasi cabang tetangga pertama hingga ujung sebelum kembali ke cabang lain.

2. Urutan kunjungan node akan berubah mengikuti urutan elemen dalam list, 
   namun tetap mempertahankan prinsip penelusuran secara mendalam.

3. DFS akan menghasilkan urutan A B D E C F (menelusuri ke bawah), 
   sedangkan BFS akan menghasilkan A B C D E F (menelusuri per level).
"""
