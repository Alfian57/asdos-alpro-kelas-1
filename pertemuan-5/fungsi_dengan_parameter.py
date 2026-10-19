# Fungsi dengan parameter memungkinkan fungsi menerima input dari luar saat dipanggil.
# Parameter adalah variabel penampung di dalam tanda kurung saat fungsi didefinisikan.
# Argumen adalah nilai nyata yang dikirimkan ke parameter saat fungsi dipanggil.

# Mendefinisikan fungsi luas_persegi_panjang dengan dua parameter: panjang dan lebar.
def luas_persegi_panjang(panjang, lebar):
    # Menghitung luas persegi panjang dengan mengalikan panjang dan lebar.
    luas = panjang * lebar
    # Menampilkan hasil perhitungan langsung ke layar.
    print(f"Luas persegi panjang adalah {luas}")


# Memanggil fungsi luas_persegi_panjang dengan argumen 10 (panjang) dan 5 (lebar).
luas_persegi_panjang(10, 5)

# Memanggil kembali fungsi dengan argumen 25 (panjang) dan 10 (lebar).
luas_persegi_panjang(25, 10)