# Soal 16: Pengecekan Usia Pembuatan KTP
# Cerita: Petugas kelurahan membutuhkan program mini untuk memverifikasi apakah
# pemohon sudah cukup umur untuk membuat Kartu Tanda Penduduk (minimal 17
# tahun).
# Spesifikasi:
# - Minta input usia dari pengguna dan konversi ke integer ke dalam variabel usia.
# - Jika usia >= 17, tampilkan pesan bahwa pengguna sudah berhak membuat
# KTP menggunakan f-string.
# - Jika kurang dari 17, tampilkan pesan bahwa usia belum mencukupi.


usia = int(input("Masukan usia: "))

if usia >= 17:
    print(f"Usia Anda {usia} tahun, Anda sudah berhak membuat KTP.")
else:
    print(f"Usia Anda {usia} tahun, usia belum mencukupi untuk membuat KTP.")
