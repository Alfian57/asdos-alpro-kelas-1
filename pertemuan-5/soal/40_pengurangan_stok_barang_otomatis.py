# Soal 40: Pengurangan Stok Barang Otomatis
# Cerita: Sebuah gudang memiliki persediaan awal 15 karung beras. Setiap kali truk
# pengantar datang, persediaan berkurang 3 karung hingga beras habis.
# Spesifikasi:
# - Inisialisasi variabel stok_beras = 15.
# - Gunakan while stok_beras > 0.
# - Kurangi stok_beras sebesar 3 pada setiap iterasi dan cetak sisa stok saat ini.
# - Setelah stok bernilai 0, cetak pesan "Stok beras habis".


stok_beras = 15

while stok_beras > 0:
    stok_beras -= 3
    print(f"Sisa stok beras saat ini: {stok_beras} karung")

print("Stok beras habis")
