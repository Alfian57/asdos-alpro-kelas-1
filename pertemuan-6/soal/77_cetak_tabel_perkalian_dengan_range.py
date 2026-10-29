# Soal 77: Cetak Tabel Perkalian dengan range()
# Cerita: Seorang siswa ingin membuat program yang mencetak hasil perkalian suatu angka
# mulai dari pengali 1 sampai 5 secara berurutan.
# Spesifikasi:
# - Minta input sebuah bilangan bulat ke dalam variabel angka.
# - Gunakan perulangan for pengali in range(1, 6):.
# - Di dalam perulangan, hitung hasil = angka * pengali dan tampilkan dengan f-string
# "{angka} x {pengali} = {hasil}".


angka = int(input("Masukan sebuah bilangan bulat: "))

for pengali in range(1, 6):
    hasil = angka * pengali
    print(f"{angka} x {pengali} = {hasil}")
