# Kalkulator sederhana yang menerima dua angka dan operator dari pengguna.
# Program menggunakan percabangan if-elif-else untuk memilih operasi yang sesuai.

# Menerima angka pertama dari pengguna; float() digunakan agar mendukung angka desimal.
angka_pertama = float(input("Masukan angka pertama : "))

# Menerima operator dari pengguna; input() menghasilkan string seperti "+", "-", "*", atau "/".
operator = input("Masukan operator [+ - * /] : ")

# Menerima angka kedua dari pengguna.
angka_kedua = float(input("Masukan angka kedua : "))

# Periksa operator yang dimasukkan dan jalankan operasi yang sesuai.
if operator == "+":
    hasil = angka_pertama + angka_kedua
    print(f"{angka_pertama} + {angka_kedua} = {hasil}")

elif operator == "-":
    hasil = angka_pertama - angka_kedua
    print(f"{angka_pertama} - {angka_kedua} = {hasil}")

elif operator == "*":
    hasil = angka_pertama * angka_kedua
    print(f"{angka_pertama} * {angka_kedua} = {hasil}")

elif operator == "/":
    # Pembagian dengan nol tidak diperbolehkan secara matematika, sehingga perlu dicek.
    if angka_kedua == 0:
        print("Error: tidak bisa membagi dengan nol")
    else:
        hasil = angka_pertama / angka_kedua
        print(f"{angka_pertama} / {angka_kedua} = {hasil}")

# Jika operator bukan salah satu dari +, -, *, atau /, tampilkan pesan kesalahan.
else:
    print("Error: operator tidak didukung")
