# Soal 34: Tebak Angka Rahasia
# Cerita: Sebuah permainan sederhana meminta pengguna menebak angka rahasia
# (misal angka 7). Program akan terus meminta tebakan sampai pengguna berhasil
# menebak angka tersebut.
# Spesifikasi:
# - Tetapkan angka rahasia pada variabel angka_rahasia = 7.
# - Gunakan while True untuk meminta input tebakan (int) dari pengguna.
# - Jika tebakan sama dengan angka_rahasia, tampilkan pesan selamat lalu
# hentikan perulangan dengan break.
# - Jika salah, tampilkan pesan bahwa tebakan masih salah.


angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka: "))
    if tebakan == angka_rahasia:
        print("Selamat, tebakan Anda benar!")
        break
    else:
        print("Tebakan masih salah, coba lagi.")
