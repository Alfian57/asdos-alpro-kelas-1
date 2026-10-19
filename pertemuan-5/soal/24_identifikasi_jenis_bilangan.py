# Soal 24: Identifikasi Jenis Bilangan
# Cerita: Program matematika dasar perlu mengidentifikasi apakah bilangan yang
# dimasukkan pengguna bernilai positif, negatif, atau tepat nol.
# Spesifikasi:
# - Minta input bilangan bulat (int) ke dalam variabel angka.
# - Gunakan if-elif-else untuk memeriksa apakah angka > 0, angka < 0, atau
# angka == 0.
# - Tampilkan kategori bilangan tersebut ke layar dengan f-string.


angka = int(input("Masukan bilangan bulat: "))

if angka > 0:
    print(f"{angka} adalah bilangan positif.")
elif angka < 0:
    print(f"{angka} adalah bilangan negatif.")
else:
    print(f"{angka} adalah tepat nol.")
