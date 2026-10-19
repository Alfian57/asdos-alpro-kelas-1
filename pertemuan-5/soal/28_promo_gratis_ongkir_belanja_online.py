# Soal 28: Promo Gratis Ongkir Belanja Online
# Cerita: Toko daring memberikan gratis ongkir jika total belanja minimal Rp50.000
# dan pembeli memiliki status member ("y").
# Spesifikasi:
# - Minta input total belanja (int) dan status member ("y" atau "n").
# - Gunakan operator logika and: jika total_belanja >= 50000 and status_member
# == "y", tampilkan "Mendapatkan promo gratis ongkir".
# - Jika tidak memenuhi, tampilkan "Ongkos kirim normal".


total_belanja = int(input("Masukan total belanja: "))
status_member = input("Apakah member [y/n]: ")

if total_belanja >= 50000 and status_member == "y":
    print("Mendapatkan promo gratis ongkir")
else:
    print("Ongkos kirim normal")
