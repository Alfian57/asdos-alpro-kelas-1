# Program ini menghitung luas persegi panjang berdasarkan input dari pengguna.
# input() menerima teks yang diketik pengguna dan selalu menghasilkan string.
# int() digunakan untuk mengubah string tersebut menjadi integer agar bisa dikalikan.
panjang = int(input("Masukan panjang : "))
lebar = int(input("Masukan lebar : "))

# Kalikan panjang dan lebar untuk mendapatkan luas.
luas = panjang * lebar

# f-string menyisipkan nilai variabel luas langsung ke dalam teks yang ditampilkan.
print(f"Luas persegi panjang: {luas} cm2")
