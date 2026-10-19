# Soal 27: Penilaian Batas Lulus Kehadiran
# Cerita: Mahasiswa diperbolehkan mengikuti ujian akhir semester jika persentase
# kehadirannya minimal 75%.
# Spesifikasi:
# - Minta input persentase kehadiran (float) ke dalam variabel kehadiran.
# - Jika kehadiran >= 75.0, tampilkan pesan diizinkan mengikuti ujian.
# - Jika di bawah 75.0, tampilkan pesan dilarang mengikuti ujian karena
# kehadiran kurang.


kehadiran = float(input("Masukan persentase kehadiran: "))

if kehadiran >= 75.0:
    print(f"Kehadiran {kehadiran}%: Diizinkan mengikuti ujian.")
else:
    print(f"Kehadiran {kehadiran}%: Dilarang mengikuti ujian karena kehadiran kurang.")
