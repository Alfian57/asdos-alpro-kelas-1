# Program menu interaktif untuk menghitung luas bangun datar secara berulang.
# Menggunakan while True agar menu kembali muncul setelah setiap perhitungan selesai.

while True:
    print("\n1. Persegi")
    print("2. Persegi Panjang")
    print("3. Keluar")

    bangun_datar = input("Masukan bangun datar [1-2] : ")

    # Pilihan 1: Hitung luas persegi (sisi * sisi).
    if bangun_datar == "1":
        sisi = int(input("\nMasukan sisi : "))

        luas = sisi * sisi
        print(f"Luas persegi adalah {luas} cm2")

    # Pilihan 2: Hitung luas persegi panjang (panjang * lebar).
    elif bangun_datar == "2":
        panjang = int(input("\nMasukan panjang : "))
        lebar = int(input("Masukan lebar : "))

        luas = panjang * lebar
        print(f"Luas persegi panjang adalah {luas} cm2")

    # Pilihan 3: Hentikan perulangan untuk keluar dari program.
    elif bangun_datar == "3":
        break

    # Tampilkan pesan jika input tidak ada dalam menu.
    else:
        print("Input tidak valid")

