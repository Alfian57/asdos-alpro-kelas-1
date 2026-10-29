# Soal 70: Pembaruan dan Cetak Daftar Tamu
# Cerita: Sekretariat himpunan mahasiswa memiliki daftar tiga tamu undangan. Tamu kedua
# mengonfirmasi pergantian perwakilan, lalu sekretaris perlu mencetak ulang daftar tamu satu
# per satu.
# Spesifikasi:
# - Buat list daftar_tamu = ["doni", "eka", "fajar"].
# - Ganti elemen indeks ke-1 (daftar_tamu[1]) menjadi "gilang".
# - Gunakan perulangan for tamu in daftar_tamu: untuk menampilkan setiap nama tamu
# ke layar.


daftar_tamu = ["doni", "eka", "fajar"]
daftar_tamu[1] = "gilang"

for tamu in daftar_tamu:
    print(tamu)
