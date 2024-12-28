import pandas as pd
import time
import matplotlib.pyplot as plt

# Fungsi Bubble Sort Iteratif
def bubble_sort_iterative(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][key] > arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Fungsi Bubble Sort Rekursif
def bubble_sort_recursive(arr, n, key):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i][key] > arr[i + 1][key]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort_recursive(arr, n - 1, key)

if __name__ == "__main__":
    # Data produk minimarket
    products = [
        {"id": 101, "name": "Milk", "price": 15000, "quantity": 20, "category": "Minuman"},
        {"id": 102, "name": "Bread", "price": 12000, "quantity": 15, "category": "Makanan"},
        {"id": 103, "name": "Shampoo", "price": 25000, "quantity": 10, "category": "Sabun"},
        {"id": 104, "name": "Apple", "price": 5000, "quantity": 50, "category": "Buah"},
        {"id": 105, "name": "Toothpaste", "price": 10000, "quantity": 25, "category": "Sabun"},
        {"id": 106, "name": "Cheese", "price": 20000, "quantity": 5, "category": "Makanan"},
        {"id": 107, "name": "Orange Juice", "price": 18000, "quantity": 30, "category": "Minuman"},
        {"id": 108, "name": "Soap", "price": 8000, "quantity": 40, "category": "Sabun"}
    ]

    # Gandakan data untuk mendapatkan ukuran data lebih besar
    products = products * 100

    # List untuk menyimpan hasil
    all_results = []

    # Loop input sebanyak 5 kali
    for run in range(1, 6):
        print(f"\nRun {run} - Masukkan ukuran input (n):")
        try:
            n = int(input("Masukkan nilai n: "))
            if n > len(products):
                print(f"Nilai n terlalu besar! Maksimal: {len(products)}")
                continue

            # Ambil data sesuai ukuran input (n)
            sample_data = products[:n]

            # Iterative
            start_time_iterative = time.perf_counter()
            bubble_sort_iterative(sample_data.copy(), "category")
            exec_time_iterative = time.perf_counter() - start_time_iterative

            # Recursive
            start_time_recursive = time.perf_counter()
            bubble_sort_recursive(sample_data.copy(), len(sample_data), "category")
            exec_time_recursive = time.perf_counter() - start_time_recursive

            # Simpan hasil untuk setiap run
            all_results.append((n, exec_time_recursive, exec_time_iterative))

            # Konversi hasil ke DataFrame
            df = pd.DataFrame(all_results, columns=['n', 'Recursive Time (s)', 'Iterative Time (s)'])

            # Tampilkan hasil di terminal
            print(df.to_string(index=False))

           # Buat grafik
            plt.figure(figsize=(10, 6))

            # Plot Recursive
            plt.plot(df['n'], df['Recursive Time (s)'], label='Recursive', color='red', marker='o', linestyle='-', linewidth=2)

            # Plot Iterative
            plt.plot(df['n'], df['Iterative Time (s)'], label='Iterative', color='blue', marker='o', linestyle='-', linewidth=2)

            # Tambahkan label, judul, dan legenda
            plt.title('Perbandingan Waktu Eksekusi Bubble Sort')
            plt.xlabel('Ukuran Input (n)')
            plt.ylabel('Waktu Eksekusi (detik)')
            plt.legend()
            plt.grid(True)

            # Mengatur sumbu Y untuk menampilkan waktu dalam format yang diinginkan
            plt.yticks([i * 0.0001 for i in range(int(max(df['Iterative Time (s)'])*10000) + 1)])

            plt.tight_layout()

            # Tampilkan grafik
            plt.show()
        except ValueError:
            print("Masukkan angka yang valid!")

    print("\nProgram selesai!")