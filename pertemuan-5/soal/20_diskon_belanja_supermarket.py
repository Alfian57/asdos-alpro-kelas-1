# Soal 20: Diskon Belanja Supermarket
# Cerita: Supermarket memberikan potongan harga langsung sebesar Rp15.000 jika
# total belanja pelanggan mencapai Rp100.000 atau lebih.
# Spesifikasi:
# - Minta input total belanja (int) ke dalam variabel total_belanja.
# - Jika total_belanja >= 100000, kurangi total belanja dengan 15000.
# - Tampilkan total pembayaran akhir menggunakan f-string.


total_belanja = int(input("Masukan total belanja: "))

if total_belanja >= 100000:
    total_belanja -= 15000

print(f"Total pembayaran akhir: Rp{total_belanja}")
