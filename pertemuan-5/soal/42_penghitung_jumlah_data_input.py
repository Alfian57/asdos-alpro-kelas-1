# Soal 42: Penghitung Jumlah Data Input
# Cerita: Petugas sensus memasukkan data umur warga satu demi satu. Penginputan
# data akan berakhir jika petugas memasukkan angka -1.
# Spesifikasi:
# - Inisialisasi variabel jumlah_orang = 0.
# - Gunakan while True untuk menerima input data umur (int).
# - Jika input bernilai -1, hentikan perulangan dengan break.
# - Jika input bukan -1, tambahkan jumlah_orang sebanyak 1.
# - Tampilkan total orang yang berhasil dicatat setelah loop selesai.


jumlah_orang = 0

while True:
    umur = int(input("Masukan data umur (-1 untuk selesai): "))
    if umur == -1:
        break
    jumlah_orang += 1

print(f"Total orang yang berhasil dicatat: {jumlah_orang}")
