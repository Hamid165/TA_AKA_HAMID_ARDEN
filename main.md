# Tugas Akhir: Analisis Kompleksitas Algoritma

## Anggota:
- **Hamid Sabirin** (2311102129)
- **Danendra Arden Shaduq** (2311102146)

---

## Perbandingan Waktu Eksekusi Bubble Sort (Iteratif vs Rekursif)

Proyek ini membandingkan waktu eksekusi antara dua implementasi algoritma **Bubble Sort**, yaitu versi **iteratif** dan **rekursif**. Pengguna dapat memasukkan ukuran input dan melihat perbandingan waktu eksekusi serta hasilnya dalam bentuk grafik.

## Fitur Utama
- Implementasi algoritma **Bubble Sort** baik secara **iteratif** maupun **rekursif**.
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

## Output Terminal

```plaintext
Run 1 - Masukkan ukuran input (n):
Masukkan nilai n: 5
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000012            0.000026
```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Figure_1.png)

```plaintext
Run 2 - Masukkan ukuran input (n):
Masukkan nilai n: 10
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000012            0.000026
10            0.000019            0.000034
```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Figure_2.png)

```plaintext
Run 3 - Masukkan ukuran input (n):
Masukkan nilai n: 15
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000012            0.000026
10            0.000019            0.000034
15            0.000031            0.000048
```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Figure_3.png)

```plaintext
Run 4 - Masukkan ukuran input (n):
Masukkan nilai n: 20
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000012            0.000026
10            0.000019            0.000034
15            0.000031            0.000048
20            0.000059            0.000069
```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Figure_4.png)

```plaintext
Run 5 - Masukkan ukuran input (n):
Masukkan nilai n: 25
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000012            0.000026
10            0.000019            0.000034
15            0.000031            0.000048
20            0.000059            0.000069
25            0.000088            0.000164
```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Figure_5.png)

Program selesai!
```
