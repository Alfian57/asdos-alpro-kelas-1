# Soal 17: Penentuan Bilangan Ganjil atau Genap
# Cerita: Seorang guru SD ingin membantu muridnya memeriksa apakah suatu angka
# yang dimasukkan tergolong bilangan ganjil atau genap.
# Spesifikasi:
# - Minta input sebuah bilangan bulat ke dalam variabel bilangan.
# - Periksa sisa bagi bilangan tersebut dengan 2 (bilangan % 2).
# - Tampilkan pesan f-string yang menyatakan apakah bilangan tersebut bernilai
# genap atau ganjil.


bilangan = int(input("Masukan bilangan bulat: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")
