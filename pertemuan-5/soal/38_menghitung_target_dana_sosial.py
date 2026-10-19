# Soal 38: Menghitung Target Dana Sosial
# Cerita: Panitia bakti sosial mengumpulkan donasi hingga mencapai target minimal
# Rp100.000. Program terus meminta nominal donasi baru hingga target terpenuhi.
# Spesifikasi:
# - Inisialisasi variabel dana_terkumpul = 0.
# - Gunakan perulangan while dana_terkumpul < 100000.
# - Minta input nominal donasi (int) dan tambahkan ke dana_terkumpul.
# - Tampilkan total dana terkumpul saat ini.
# - Setelah perulangan berhenti, tampilkan pesan bahwa target donasi telah
# tercapai.


dana_terkumpul = 0

while dana_terkumpul < 100000:
    donasi = int(input("Masukan nominal donasi: "))
    dana_terkumpul += donasi
    print(f"Total dana terkumpul saat ini: Rp{dana_terkumpul}")

print("Target donasi telah tercapai!")
