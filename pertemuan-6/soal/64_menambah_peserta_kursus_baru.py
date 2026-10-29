# Soal 64: Menambah Peserta Kursus Baru
# Cerita: Lembaga kursus bahasa memiliki daftar peserta awal. Ketika ada satu pendaftar baru
# yang datang ke meja administrasi, petugas langsung menambahkan namanya ke dalam daftar.
# Spesifikasi:
# - Buat list daftar_peserta = ["andi", "budi", "citra"].
# - Minta input nama peserta baru dari pengguna ke dalam variabel peserta_baru.
# - Tambahkan peserta_baru ke dalam daftar_peserta menggunakan .append().
# - Tampilkan isi daftar_peserta terbaru ke layar.


daftar_peserta = ["andi", "budi", "citra"]
peserta_baru = input("Masukan nama peserta baru: ")
daftar_peserta.append(peserta_baru)
print(daftar_peserta)
