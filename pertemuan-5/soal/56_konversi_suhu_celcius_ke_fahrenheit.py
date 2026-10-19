# Soal 56: Konversi Suhu Celcius ke Fahrenheit
# Cerita: Petugas stasiun cuaca membutuhkan fungsi yang menghitung dan
# mengembalikan nilai konversi dari satuan derajat Celcius ke Fahrenheit.
# Spesifikasi:
# - Buat fungsi dengan return celcius_ke_fahrenheit(suhu_c).
# - Menerima parameter suhu_c (float).
# - Hitung nilai Fahrenheit dengan rumus (suhu_c * 1.8) + 32.
# - Kembalikan (return) hasil perhitungan tersebut.


def celcius_ke_fahrenheit(suhu_c):
    return (suhu_c * 1.8) + 32


hasil = celcius_ke_fahrenheit(25.0)
print(f"Suhu Fahrenheit: {hasil}")
