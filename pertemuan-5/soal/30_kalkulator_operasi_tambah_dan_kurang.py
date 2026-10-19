# Soal 30: Kalkulator Operasi Tambah dan Kurang
# Cerita: Program kalkulator sederhana dapat menghitung operasi penjumlahan atau
# pengurangan berdasarkan pilihan simbol dari pengguna.
# Spesifikasi:
# - Minta input dua buah bilangan desimal (float) dan satu simbol operator ("+"
# atau "-").
# - Jika operator "+", tampilkan hasil penjumlahan kedua bilangan.
# - Jika operator "-", tampilkan hasil pengurangan kedua bilangan.
# - Jika selain keduanya, tampilkan pesan bahwa operator tidak didukung.


angka1 = float(input("Masukan bilangan pertama: "))
angka2 = float(input("Masukan bilangan kedua: "))
operator = input("Masukan simbol operator (+/-): ")

if operator == "+":
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"{angka1} - {angka2} = {hasil}")
else:
    print("Operator tidak didukung")
