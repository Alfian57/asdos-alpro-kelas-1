# Soal 23: Peringatan Termometer Digital
# Cerita: Termometer digital di pintu masuk gedung akan memeriksa suhu badan
# pengunjung. Jika suhu 37.5 derajat Celsius atau lebih, pengunjung diminta beristirahat
# di pos kesehatan.
# Spesifikasi:
# - Minta input suhu badan (float) ke dalam variabel suhu.
# - Jika suhu >= 37.5, tampilkan pesan peringatan bahwa suhu tubuh tinggi.
# - Jika suhu < 37.5, tampilkan pesan bahwa suhu normal dan dipersilakan
# masuk.


suhu = float(input("Masukan suhu badan: "))

if suhu >= 37.5:
    print(f"Peringatan: Suhu tubuh tinggi ({suhu}°C), silakan istirahat di pos kesehatan.")
else:
    print(f"Suhu normal ({suhu}°C), dipersilakan masuk.")
