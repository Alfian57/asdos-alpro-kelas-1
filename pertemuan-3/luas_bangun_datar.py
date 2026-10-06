# Program ini menghitung luas bangun datar berdasarkan pilihan pengguna.
# Pengguna memilih jenis bangun datar, lalu memasukkan ukurannya.
# Program menggunakan if-elif-else untuk menentukan rumus mana yang dipakai.

# Tampilkan daftar pilihan bangun datar yang tersedia.
print("1. Persegi")
print("2. Persegi Panjang")

# input() selalu menghasilkan string, sehingga pilihan disimpan sebagai "1" atau "2".
bangun_datar = input("Masukan bangun datar [1-2] : ")

# Jika pengguna memilih "1", hitung luas persegi.
if bangun_datar == "1":
    # int() mengubah input string menjadi integer agar bisa digunakan dalam operasi hitung.
    sisi = int(input("Masukan sisi : "))

    # Luas persegi = sisi × sisi.
    luas = sisi * sisi
    print(f"Luas persegi adalah {luas} cm2")

# Jika pengguna memilih "2", hitung luas persegi panjang.
elif bangun_datar == "2":
    panjang = int(input("Masukan panjang : "))
    lebar = int(input("Masukan lebar : "))

    # Luas persegi panjang = panjang × lebar.
    luas = panjang * lebar
    print(f"Luas persegi panjang adalah {luas} cm2")

# Jika input bukan "1" atau "2", tampilkan pesan kesalahan.
else:
    print("Input tidak valid")
