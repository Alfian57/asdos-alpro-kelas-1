# Soal 45: Cetak Pola Karakter Berulang
# Cerita: Pengguna ingin mencetak karakter pagar ("#") sebanyak N baris sesuai
# jumlah yang ia inginkan ke layar terminal.
# Spesifikasi:
# - Minta input jumlah baris (int) ke dalam variabel jumlah_baris.
# - Inisialisasi variabel baris = 1.
# - Gunakan while baris <= jumlah_baris untuk mencetak karakter "#".
# - Tambahkan nilai baris sebanyak 1 pada setiap iterasi.


jumlah_baris = int(input("Masukan jumlah baris: "))
baris = 1

while baris <= jumlah_baris:
    print("#")
    baris += 1
