import pandas as pd
import time

def merge(left, right, key):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort_iterative(arr, key):
    n = len(arr)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right, key)
        width *= 2
    return arr

def merge_sort_recursive(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid], key)
    right = merge_sort_recursive(arr[mid:], key)
    return merge(left, right, key)


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

    products = products * 100
    key = "category"  # Mengurutkan berdasarkan kategori produk

    # Hasil perbandingan waktu iteratif dan rekursif
    results = []

    for i in range(5):
        start_time_iterative = time.perf_counter()
        merge_sort_iterative(products.copy(), key)
        execution_time_iterative = time.perf_counter() - start_time_iterative

        start_time_recursive = time.perf_counter()
        merge_sort_recursive(products.copy(), key)
        execution_time_recursive = time.perf_counter() - start_time_recursive

        results.append((execution_time_iterative, execution_time_recursive))

    # Mengonversi hasil ke DataFrame
    df = pd.DataFrame(results, columns=['Iterative (s)', 'Recursive (s)'])

    # Menampilkan hasil di terminal dalam bentuk tabel
    print(f"+------|------------------|------------------+")
    print(f"| Run  | Iterative (s)    | Recursive (s)    |")
    print(f"+------|------------------|------------------+")
    for i, (iter_time, rec_time) in enumerate(results, 1):
        print(f"|{i:<4}  | {iter_time:<16.6f} | {rec_time:<16.6f} |")
    print(f"+------|------------------|------------------+")

    # Menyimpan ke Excel, menggantikan data yang ada
    file_path = r"C:\Users\ACER\Documents\FOLDER SEMESTER KULIAH\SEMESTER 3\AKA\tubes.xlsx"
    
    try:
        # Menghapus data lama dan menyimpan data baru
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, sheet_name='Results', index_label='Run')
        print(f"Hasil berhasil disimpan di {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan ke Excel: {e}")