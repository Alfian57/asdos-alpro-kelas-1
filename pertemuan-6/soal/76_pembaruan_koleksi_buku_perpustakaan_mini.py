# Soal 76: Pembaruan Koleksi Buku Perpustakaan Mini
# Cerita: Pengelola taman bacaan baru saja menerima sumbangan satu buku baru dan harus
# menarik satu buku lama yang rusak dari daftar koleksi, kemudian menampilkan daftar buku
# terkini.
# Spesifikasi:
# - Buat list koleksi_buku = ["komik", "novel", "kamus"].
# - Tambahkan "ensiklopedia" ke dalam list menggunakan .append().
# - Hapus "novel" dari dalam list menggunakan .remove().
# - Gunakan perulangan for buku in koleksi_buku: untuk menampilkan setiap buku yang
# tersedia.


koleksi_buku = ["komik", "novel", "kamus"]
koleksi_buku.append("ensiklopedia")
koleksi_buku.remove("novel")

for buku in koleksi_buku:
    print(buku)
