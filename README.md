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
 5            0.000031             0.00015

```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Grafik_1.png)

```plaintext
Run 2 - Masukkan ukuran input (n):
Masukkan nilai n: 20
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000031             0.00015
20            0.000088             0.00030

```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Grafik_2.png)

```plaintext
Run 3 - Masukkan ukuran input (n):
Masukkan nilai n: 40
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000031             0.00015
20            0.000088             0.00030
40            0.000225             0.00047
```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Grafik_3.png)

```plaintext
Run 4 - Masukkan ukuran input (n):
Masukkan nilai n: 60
 n  Recursive Time (s)  Iterative Time (s)
 5            0.000031            0.000150
20            0.000088            0.000300
40            0.000225            0.000470
60            0.000675            0.000766
```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Grafik_4.png)

```plaintext
Run 5 - Masukkan ukuran input (n):
Masukkan nilai n: 100
  n  Recursive Time (s)  Iterative Time (s)
  5            0.000031            0.000150
 20            0.000088            0.000300
 40            0.000225            0.000470
 60            0.000675            0.000766
100            0.001901            0.001830
```
### Output Grafik
![output](https://github.com/Hamid165/TA_AKA_HAMID_ARDEN/blob/main/Grafik_5.png)

Program selesai!
```
