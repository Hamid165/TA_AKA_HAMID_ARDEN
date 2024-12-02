import pandas as pd
import matplotlib.pyplot as plt

# Path ke file Excel
file_path = r"C:\Users\ACER\Documents\FOLDER SEMESTER KULIAH\SEMESTER 3\AKA\tubes.xlsx"

# Baca file Excel
data = pd.read_excel(file_path)

# Normalisasi nama kolom
data.columns = data.columns.str.strip()  # Menghapus spasi tambahan di awal/akhir

# Verifikasi nama kolom
print(data.columns)

# Buat grafik garis
plt.figure(figsize=(8, 6))
plt.plot(data['Run'], data['Iterative (s)'], marker='o', label='Iterative (s)', color='blue')
plt.plot(data['Run'], data['Recursive (s)'], marker='s', label='Recursive (s)', color='red')

# Tambahkan detail grafik
plt.title("Running time kompleksitas t(n) ", fontsize=14)
plt.xlabel("Run", fontsize=12)
plt.ylabel("Time (s)", fontsize=12)
plt.xticks(data['Run'])
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Simpan dan tampilkan grafik
plt.tight_layout()
plt.savefig("comparison_graph.png")  # Simpan sebagai file gambar
plt.show()
