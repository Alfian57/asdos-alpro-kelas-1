# Soal 67: Cetak Daftar Barang Gudang
# Cerita: Petugas gudang ingin menampilkan setiap nama barang yang tersimpan di dalam
# daftar inventaris satu per satu ke layar agar mudah diperiksa.
# Spesifikasi:
# - Buat list list_barang = ["radio", "kertas", "kursi"].
# - Gunakan perulangan for barang in list_barang: untuk membaca setiap elemen.
# - Tampilkan setiap elemen dengan format f-string "Barang: {barang}".


list_barang = ["radio", "kertas", "kursi"]

for barang in list_barang:
    print(f"Barang: {barang}")
