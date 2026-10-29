# List adalah struktur data yang digunakan untuk menyimpan kumpulan nilai dalam satu variabel.
# Elemen pada list dapat diakses berdasarkan nomor indeksnya yang dimulai dari indeks 0.

# Membuat list dengan elemen awal nama mahasiswa.
daftar_nama_mahasiwa = ["fahmi", "raja", "rafli"]

# Menampilkan seluruh isi list.
print(daftar_nama_mahasiwa)

# Menampilkan elemen list berdasarkan indeks tertentu.
print(daftar_nama_mahasiwa[0])
print(daftar_nama_mahasiwa[1])
print(daftar_nama_mahasiwa[2])

# Mengubah nilai elemen list pada indeks tertentu.
# daftar_nama_mahasiwa[0] = "rusli"
print(daftar_nama_mahasiwa)

# Menambahkan elemen baru ke akhir list menggunakan append().
daftar_nama_mahasiwa.append("shabrina")
print(daftar_nama_mahasiwa)

# Menghapus elemen dari list berdasarkan nilainya menggunakan remove().
daftar_nama_mahasiwa.remove("rafli")
print(daftar_nama_mahasiwa)
