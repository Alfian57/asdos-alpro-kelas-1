# Soal 18: Ambang Kelulusan Ujian Teori
# Cerita: Sistem penilaian kursus komputer menetapkan bahwa peserta ujian
# dinyatakan lulus jika mendapatkan nilai minimal 70.
# Spesifikasi:
# - Minta input nilai ujian berupa angka desimal (float) ke dalam variabel
# nilai_ujian.
# - Jika nilai_ujian >= 70.0, tampilkan "Status: Lulus" beserta nilainya.
# - Jika di bawah 70.0, tampilkan "Status: Tidak Lulus" beserta nilainya.


nilai_ujian = float(input("Masukan nilai ujian: "))

if nilai_ujian >= 70.0:
    print(f"Status: Lulus dengan nilai {nilai_ujian}")
else:
    print(f"Status: Tidak Lulus dengan nilai {nilai_ujian}")
