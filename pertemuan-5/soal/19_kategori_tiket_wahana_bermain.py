# Soal 19: Kategori Tiket Wahana Bermain
# Cerita: Wahana permainan taman hiburan memberlakukan tarif tiket berbeda:
# pengunjung dengan tinggi badan di bawah 120 cm membayar tarif anak Rp25.000,
# sedangkan tinggi 120 cm ke atas membayar tarif dewasa Rp40.000.
# Spesifikasi:
# - Minta input tinggi badan dalam cm (int) ke dalam variabel tinggi_badan.
# - Gunakan percabangan if-else untuk menentukan harga tiket.
# - Tampilkan kategori dan harga tiket yang harus dibayar menggunakan f-string.


tinggi_badan = int(input("Masukan tinggi badan (cm): "))

if tinggi_badan < 120:
    kategori = "Anak"
    harga = 25000
else:
    kategori = "Dewasa"
    harga = 40000

print(f"Kategori: {kategori}, Harga tiket: Rp{harga}")
