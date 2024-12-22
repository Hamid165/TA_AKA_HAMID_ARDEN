# Tugas Akhir: Analisis Kompleksitas Algoritma

## Anggota:
- **Hamid Sabirin** (2311102129)
- **Danendra Arden Shaduq** (2311102146)

---

## Perbandingan Waktu Eksekusi Insertion Sort (Iteratif vs Rekursif)

Proyek ini membandingkan waktu eksekusi antara dua implementasi algoritma **Insertion Sort**, yaitu versi **iteratif** dan **rekursif**. Pengguna dapat memasukkan ukuran input dan melihat perbandingan waktu eksekusi serta hasilnya dalam bentuk grafik.

## Fitur Utama
- Implementasi algoritma **Insertion Sort** baik secara **iteratif** maupun **rekursif**.
- Pengguna dapat menginputkan ukuran data yang diinginkan (`n`).
- Menampilkan hasil perbandingan waktu eksekusi dalam bentuk tabel yang rapi dan grafik.
- Mencetak hasil tabel dengan garis untuk kejelasan.



```python
### Fungsi insertion_sort_iterative(arr, key)

def insertion_sort_iterative(arr, key):
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > current_element[key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element
    return arr

### Fungsi insertion_sort_recursive(arr, n, key)

def insertion_sort_recursive(arr, n, key):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1, key)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j][key] > last[key]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last
```

## output terminal
Run 1 - Masukkan ukuran input (n):
Masukkan nilai n: 5
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000021             0.00003

Run 2 - Masukkan ukuran input (n):
Masukkan nilai n: 10
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000021            0.000030
10            0.000035            0.000114

Run 3 - Masukkan ukuran input (n):
Masukkan nilai n: 15
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000021            0.000030
10            0.000035            0.000114
15            0.000023            0.000035

Run 4 - Masukkan ukuran input (n):
Masukkan nilai n: 20
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000021            0.000030
10            0.000035            0.000114
15            0.000023            0.000035
20            0.000043            0.000053

Run 5 - Masukkan ukuran input (n):
Masukkan nilai n: 25
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000021            0.000030
10            0.000035            0.000114
15            0.000023            0.000035
20            0.000043            0.000053
25            0.000091            0.000240

Program selesai!

### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/grafik.png)