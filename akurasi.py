import pandas as pd

# 1. Membaca file CSV
# Pastikan nama file sesuai dengan file Anda
df = pd.read_csv('Data Ktp - Sheet1.csv')

# 2. Membersihkan dan Menyiapkan Data
# Mengubah kolom NIK menjadi string agar tidak dianggap angka (menghindari masalah format)
df['NIK'] = df['NIK'].astype(str).str.strip()
df['Nik Asli'] = df['Nik Asli'].astype(str).str.strip()

# Membersihkan spasi di awal/akhir nama untuk perbandingan yang akurat
df['NAMA'] = df['NAMA'].astype(str).str.strip()
df['Nama Asli'] = df['Nama Asli'].astype(str).str.strip()

# 3. Melakukan Pengecekan
# Membuat kolom baru 'Cek_NIK' yang bernilai True jika sama, False jika beda
df['Cek_NIK'] = df['NIK'] == df['Nik Asli']

# Membuat kolom baru 'Cek_Nama' yang bernilai True jika sama, False jika beda
df['Cek_Nama'] = df['NAMA'] == df['Nama Asli']

# 4. Menampilkan Hasil
# Menampilkan kolom-kolom terkait untuk verifikasi
hasil_cek = df[['NIK', 'Nik Asli', 'Cek_NIK', 'NAMA', 'Nama Asli', 'Cek_Nama']]

print("Hasil Pengecekan:")
print(hasil_cek)

# Menampilkan data yang TIDAK cocok (jika ada)
mismatch = df[(df['Cek_NIK'] == False) | (df['Cek_Nama'] == False)]

if not mismatch.empty:
    print("\nData yang TIDAK cocok ditemukan:")
    print(mismatch[['NIK', 'Nik Asli', 'NAMA', 'Nama Asli']])
else:
    print("\nSemua data NIK dan Nama cocok (Valid).")