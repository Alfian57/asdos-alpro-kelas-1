# Soal 65: Membatalkan Pesanan Makanan
# Cerita: Pelanggan memesan tiga jenis makanan di kafe, tetapi kemudian meminta kasir untuk
# menghapus salah satu makanan dari daftar pesanan karena berubah pikiran.
# Spesifikasi:
# - Buat list pesanan = ["kopi", "roti", "kentang"].
# - Minta input nama makanan yang ingin dibatalkan ke dalam variabel batal.
# - Hapus makanan tersebut dari list pesanan menggunakan .remove().
# - Tampilkan daftar pesanan yang tersisa ke layar.


pesanan = ["kopi", "roti", "kentang"]
batal = input("Masukan nama makanan yang ingin dibatalkan: ")
pesanan.remove(batal)
print(pesanan)
