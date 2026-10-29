# Soal 71: Pendaftaran Tiga Anggota Kelompok
# Cerita: Dosen meminta ketua kelompok untuk memasukkan 3 nama anggota kelompoknya
# satu per satu melalui terminal untuk disimpan ke dalam sebuah list.
# Spesifikasi:
# - Buat list kosong anggota_kelompok = [].
# - Gunakan perulangan for urutan in range(0, 3): untuk meminta input nama anggota
# dan menambahkannya ke anggota_kelompok menggunakan .append().
# - Setelah perulangan berakhir, tampilkan seluruh isi anggota_kelompok.


anggota_kelompok = []

for urutan in range(0, 3):
    nama = input("Masukan nama anggota: ")
    anggota_kelompok.append(nama)

print(anggota_kelompok)
