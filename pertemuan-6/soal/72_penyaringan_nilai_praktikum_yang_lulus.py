# Soal 72: Penyaringan Nilai Praktikum yang Lulus
# Cerita: Asisten praktikum memiliki daftar nilai dari 5 mahasiswa. Ia ingin menampilkan
# hanya nilai-nilai yang mencapai batas kelulusan minimal 75.
# Spesifikasi:
# - Buat list daftar_nilai = [80, 65, 90, 70, 85].
# - Gunakan perulangan for nilai in daftar_nilai: untuk memeriksa setiap nilai.
# - Di dalam perulangan, gunakan if nilai >= 75: untuk mencetak nilai yang lulus beserta
# keterangannya.


daftar_nilai = [80, 65, 90, 70, 85]

for nilai in daftar_nilai:
    if nilai >= 75:
        print(f"Nilai {nilai}: Lulus")
