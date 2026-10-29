# Soal 69: Menjumlahkan Harga Belanjaan di List
# Cerita: Dinda mencatat harga tiga barang yang dibelinya di minimarket ke dalam sebuah list.
# Ia ingin menghitung total uang yang harus dibayarkan menggunakan perulangan for.
# Spesifikasi:
# - Buat list daftar_harga = [12000, 15000, 8000].
# - Inisialisasi variabel total_harga = 0.
# - Gunakan perulangan for harga in daftar_harga: untuk menambahkan setiap harga ke
# dalam total_harga.
# - Tampilkan nilai total_harga setelah perulangan selesai.


daftar_harga = [12000, 15000, 8000]
total_harga = 0

for harga in daftar_harga:
    total_harga += harga

print(total_harga)
