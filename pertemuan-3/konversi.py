# Konversi tipe data mengubah nilai dari satu tipe ke tipe lain.
# Fungsi str(), int(), dan float() digunakan untuk melakukan konversi tersebut.
# Fungsi type() mengembalikan tipe dari sebuah nilai.

# INTEGER KE STRING
# str() mengubah nilai integer menjadi string.
# Setelah konversi, angka 75 menjadi teks "75" dan tidak bisa lagi dipakai untuk operasi hitung.
berat_badan_dalam_integer = 75
berat_badan_dalam_string = str(berat_badan_dalam_integer)

# Menampilkan tipe asli (int) lalu tipe setelah konversi (str).
print(type(berat_badan_dalam_integer))
print(type(berat_badan_dalam_string))

# STRING KE INTEGER
# int() mengubah string yang berisi angka bulat menjadi integer.
# Konversi ini diperlukan agar angka yang diterima dari input() bisa dipakai untuk operasi hitung.
angka_dalam_string = "55"
angka_dalam_integer = int(angka_dalam_string)

# Menampilkan tipe asli (str) lalu tipe setelah konversi (int).
print(type(angka_dalam_string))
print(type(angka_dalam_integer))

# STRING KE FLOAT
# float() mengubah string yang berisi angka desimal menjadi float.
# Gunakan float() ketika nilai yang dikonversi memiliki bagian desimal.
tinggi_badan_dalam_string = "171.5"
tinggi_badan_dalam_float = float(tinggi_badan_dalam_string)

# Menampilkan tipe asli (str) lalu tipe setelah konversi (float).
print(type(tinggi_badan_dalam_string))
print(type(tinggi_badan_dalam_float))