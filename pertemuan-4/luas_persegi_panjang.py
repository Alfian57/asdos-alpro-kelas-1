# Program menghitung luas persegi panjang secara berulang.
# Menggunakan while True agar pengguna dapat menghitung beberapa kali sampai memilih selesai.

while True:
    panjang = int(input("\nMasukan panjang : "))
    lebar = int(input("Masukan lebar : "))

    # Luas persegi panjang = panjang * lebar.
    luas = panjang * lebar

    print(f"Luas persegi panjang: {luas} cm2")

    # Minta konfirmasi pengguna; jika input 'n', hentikan perulangan.
    ulang = input("\nApakah ingin menghitung ulang [y/n] : ")
    if ulang == "n":
        break

