# Soal 33: Total Tabungan Celengan
# Cerita: Budi menabung uang setiap hari sebesar Rp5.000 selama 7 hari berturut-turut.
# Ia ingin menghitung akumulasi saldo tabungannya hari demi hari.
# Spesifikasi:
# - Inisialisasi variabel hari = 1 dan total_tabungan = 0.
# - Gunakan perulangan while hari <= 7.
# - Tambahkan 5000 ke total_tabungan dan cetak saldo hari tersebut dengan
# f-string.
# - Tambahkan nilai hari sebanyak 1 pada setiap iterasi.


hari = 1
total_tabungan = 0

while hari <= 7:
    total_tabungan += 5000
    print(f"Hari ke-{hari}: total tabungan = Rp{total_tabungan}")
    hari += 1
