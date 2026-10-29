# Soal 73: Penambahan dan Perhitungan Total Berat Paket
# Cerita: Kurir ekspedisi sudah memiliki catatan berat 3 paket di dalam list. Sebelum
# berangkat, ada 1 paket tambahan yang masuk, lalu kurir menghitung total muatan seluruh
# paketnya.
# Spesifikasi:
# - Buat list berat_paket = [3, 5, 2].
# - Minta input berat paket baru (int) dari pengguna dan tambahkan ke berat_paket
# menggunakan .append().
# - Gunakan perulangan for dan variabel akumulator total_berat = 0 untuk menjumlahkan
# seluruh elemen di berat_paket, lalu cetak hasilnya.


berat_paket = [3, 5, 2]

berat_baru = int(input("Masukan berat paket baru: "))
berat_paket.append(berat_baru)

total_berat = 0
for berat in berat_paket:
    total_berat += berat

print(f"Total berat paket: {total_berat}")
