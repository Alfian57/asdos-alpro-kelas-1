# Fungsi dengan return mengembalikan suatu nilai hasil pemrosesan ke pemanggil fungsi.
# Berbeda dengan fungsi yang hanya mencetak dengan print(), nilai dari return dapat disimpan ke variabel atau diolah lebih lanjut.

# Mendefinisikan fungsi yang mengembalikan nilai luas persegi panjang.
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    # return mengirimkan kembali nilai variabel luas ke pemanggil fungsi.
    return luas


# Memanggil fungsi, menampung nilai return ke dalam variabel hasil_luas, lalu mencetaknya.
hasil_luas = luas_persegi_panjang(10, 5)
print(f"Luas persegi panjang adalah {hasil_luas}")

# Memanggil fungsi dengan argumen lain dan menampung kembali hasilnya ke variabel.
hasil_luas = luas_persegi_panjang(25, 10)
print(f"Luas persegi panjang adalah {hasil_luas}")