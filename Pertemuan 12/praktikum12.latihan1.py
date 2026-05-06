'''
======================================
Nama: Ibrahim Ahmad Idhofi
NIM: J0403251107
Kelas: TPL B1
======================================
'''

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
# Representasi weighted graph menggunakan dictionary bersarang


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

'''
==========================================================
Jawaban Analisis:
==========================================================
1. Berapa total bobot jalur A -> B -> D?
   Jawaban: Total bobotnya adalah 9.

2. Berapa total bobot jalur A -> C -> D?
   Jawaban: Total bobotnya adalah 3.

3. Jalur mana yang dipilih sebagai jalur terpendek?
   Jawaban: Jalur A -> C -> D.

4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
   Jawaban: Karena dalam weighted graph (graf berbobot), setiap edge memiliki "biaya" 
   atau nilai yang berbeda. Jalur dengan sedikit edge bisa saja memiliki bobot 
   individual yang sangat besar, sehingga jalur yang lebih memutar (memiliki 
   lebih banyak edge) namun dengan bobot kecil justru menghasilkan total nilai 
   akumulatif yang lebih efisien/pendek.
==========================================================
'''
