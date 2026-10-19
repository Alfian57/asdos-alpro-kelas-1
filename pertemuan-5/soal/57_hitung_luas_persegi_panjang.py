# Soal 57: Hitung Luas Persegi Panjang
# Cerita: Tukang bangunan membutuhkan fungsi pembantu untuk menghitung luas
# dinding ruangan sebelum mengecat.
# Spesifikasi:
# - Buat fungsi dengan return hitung_luas_persegi_panjang(panjang, lebar).
# - Menerima dua parameter numerik: panjang dan lebar.
# - Hitung luas dengan rumus panjang * lebar.
# - Kembalikan (return) nilai luas tersebut.


def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas


hasil = hitung_luas_persegi_panjang(10, 5)
print(f"Luas persegi panjang: {hasil}")
