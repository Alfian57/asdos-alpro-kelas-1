# Program menghitung luas segitiga menggunakan fungsi dengan parameter.
# Parameter menerima nilai alas dan tinggi yang dikirimkan saat fungsi dipanggil.

# Mendefinisikan fungsi dengan dua parameter: alas dan tinggi.
def luas_segitiga(alas, tinggi):
    # Menghitung luas segitiga dengan rumus 0.5 * alas * tinggi.
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga adalah {luas} cm2")


# Memanggil fungsi luas_segitiga dengan argumen 10 dan 5.
luas_segitiga(10, 5)

# Memanggil fungsi luas_segitiga dengan argumen 20 dan 8.
luas_segitiga(20, 8)