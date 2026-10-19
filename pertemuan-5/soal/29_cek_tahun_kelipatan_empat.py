# Soal 29: Cek Tahun Kelipatan Empat
# Cerita: Siswa ingin mengecek apakah suatu tahun merupakan tahun kabisat dasar,
# yaitu tahun yang habis dibagi 4.
# Spesifikasi:
# - Minta input tahun (int) ke dalam variabel tahun.
# - Gunakan kondisi tahun % 4 == 0 untuk memeriksa.
# - Tampilkan keterangan apakah tahun tersebut merupakan tahun kabisat atau
# bukan menggunakan f-string.


tahun = int(input("Masukan tahun: "))

if tahun % 4 == 0:
    print(f"Tahun {tahun} merupakan tahun kabisat.")
else:
    print(f"Tahun {tahun} bukan merupakan tahun kabisat.")
