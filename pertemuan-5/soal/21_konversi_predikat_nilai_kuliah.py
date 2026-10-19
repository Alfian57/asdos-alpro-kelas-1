# Soal 21: Konversi Predikat Nilai Kuliah
# Cerita: Dosen ingin mengonversi nilai angka mahasiswa ke dalam predikat huruf
# dengan aturan: nilai 85 ke atas mendapat 'A', nilai 70 sampai 84 mendapat 'B', nilai 55
# sampai 69 mendapat 'C', dan di bawah 55 mendapat 'D'.
# Spesifikasi:
# - Minta input nilai angka (float) ke dalam variabel nilai.
# - Gunakan struktur if-elif-else untuk menentukan predikat huruf.
# - Tampilkan predikat nilai yang diperoleh menggunakan f-string.


nilai = float(input("Masukan nilai angka: "))

if nilai >= 85:
    predikat = "A"
elif nilai >= 70:
    predikat = "B"
elif nilai >= 55:
    predikat = "C"
else:
    predikat = "D"

print(f"Nilai {nilai} mendapatkan predikat {predikat}")
