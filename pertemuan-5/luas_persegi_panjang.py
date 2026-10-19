# Program menghitung luas persegi panjang secara berulang menggunakan fungsi.
# Program menggabungkan fungsi perhitungan dengan perulangan while True hingga pengguna memilih berhenti.

# Mendefinisikan fungsi untuk menghitung dan mencetak luas persegi panjang.
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f"Luas persegi panjang: {luas} cm2")


# Perulangan while True agar program dapat menghitung berulang kali.
while True:
    # int() mengonversi input teks dari pengguna menjadi tipe data integer.
    panjang = int(input("\nMasukan panjang : "))
    lebar = int(input("Masukan lebar : "))

    # Memanggil fungsi luas_persegi_panjang dengan input dari pengguna.
    luas_persegi_panjang(panjang, lebar)

    # Konfirmasi apakah pengguna ingin mengulang perhitungan.
    ulang = input("\nApakah ingin menghitung ulang [y/n] : ")
    # Jika pengguna memasukkan "n", hentikan perulangan dengan break.
    if ulang == "n":
        break
