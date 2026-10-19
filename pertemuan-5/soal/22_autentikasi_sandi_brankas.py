# Soal 22: Autentikasi Sandi Brankas
# Cerita: Sebuah brankas elektronik sederhana membutuhkan verifikasi PIN angka
# rahasia ("1234") sebelum membuka pintu.
# Spesifikasi:
# - Minta input PIN dari pengguna sebagai teks (str) ke dalam variabel input_pin.
# - Jika input_pin == "1234", tampilkan pesan "Akses diterima, pintu terbuka".
# - Jika salah, tampilkan pesan "Akses ditolak, PIN salah".


input_pin = input("Masukan PIN: ")

if input_pin == "1234":
    print("Akses diterima, pintu terbuka")
else:
    print("Akses ditolak, PIN salah")
