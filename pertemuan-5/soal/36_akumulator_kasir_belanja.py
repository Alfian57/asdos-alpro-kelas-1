# Soal 36: Akumulator Kasir Belanja
# Cerita: Kasir toko kelontong memasukkan harga barang satu per satu dan
# menjumlahkannya. Input akan berhenti ketika kasir memasukkan harga 0.
# Spesifikasi:
# - Inisialisasi variabel total_belanja = 0.
# - Gunakan while True untuk menerima input harga barang (int).
# - Jika harga bernilai 0, hentikan perulangan dengan break.
# - Jika harga lebih dari 0, tambahkan ke total_belanja.
# - Setelah perulangan selesai, tampilkan total belanja akhir.


total_belanja = 0

while True:
    harga = int(input("Masukan harga barang (0 untuk selesai): "))
    if harga == 0:
        break
    elif harga > 0:
        total_belanja += harga

print(f"Total belanja akhir: Rp{total_belanja}")
