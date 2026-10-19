# Soal 39: Konfirmasi Pengulangan Hitung
# Cerita: Program menghitung perkalian dua angka yang terus berjalan berulang kali
# sampai pengguna mengetik "n" pada pertanyaan konfirmasi.
# Spesifikasi:
# - Gunakan while True.
# - Di dalam perulangan, minta input dua angka bulat dan cetak hasil
# perkaliannya.
# - Tanyakan konfirmasi kepada pengguna: "Hitung lagi? [y/n] : ".
# - Jika pengguna memasukkan "n", hentikan perulangan menggunakan break.


while True:
    angka1 = int(input("Masukan angka pertama: "))
    angka2 = int(input("Masukan angka kedua: "))
    hasil = angka1 * angka2
    print(f"Hasil perkalian: {hasil}")

    konfirmasi = input("Hitung lagi? [y/n] : ")
    if konfirmasi == "n":
        break
