# Soal 26: Menu Pilihan Minuman
# Cerita: Kedai minuman memiliki menu sederhana: nomor 1 untuk Es Kopi
# (Rp10.000) dan nomor 2 untuk Es Teh (Rp5.000).
# Spesifikasi:
# - Minta input nomor pilihan menu (str) ke dalam variabel pilihan.
# - Gunakan if-elif-else: jika "1" tampilkan rincian Es Kopi, jika "2" tampilkan
# rincian Es Teh, selain itu tampilkan "Menu tidak tersedia".


pilihan = input("Masukan nomor pilihan menu (1/2): ")

if pilihan == "1":
    print("Es Kopi - Rp10.000")
elif pilihan == "2":
    print("Es Teh - Rp5.000")
else:
    print("Menu tidak tersedia")
