# Soal 75: Fungsi Hitung Total Donasi dari List
# Cerita: Bendahara kegiatan amal membutuhkan fungsi yang menerima daftar nominal donasi
# dalam bentuk list dan mengembalikan hasil penjumlahan seluruh donasi tersebut.
# Spesifikasi:
# - Buat fungsi hitung_total_donasi(list_donasi) yang menerima parameter berupa list
# angka.
# - Di dalam fungsi, gunakan variabel total = 0 dan perulangan for nominal in
# list_donasi: untuk menjumlahkan seluruh donasi.
# - Kembalikan (return) nilai total dan tampilkan hasilnya saat fungsi dipanggil dengan
# list [20000, 50000, 30000].


def hitung_total_donasi(list_donasi):
    total = 0
    for nominal in list_donasi:
        total += nominal
    return total


total = hitung_total_donasi([20000, 50000, 30000])
print(f"Total donasi: Rp{total}")
