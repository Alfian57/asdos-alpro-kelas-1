# Soal 51: Sapaan Personal Mahasiswa
# Cerita: Sistem portal akademik ingin menyapa setiap mahasiswa yang login dengan
# menyebutkan nama lengkapnya di layar.
# Spesifikasi:
# - Buat fungsi dengan parameter sapa_mahasiswa(nama).
# - Fungsi menerima satu parameter nama bertipe string dan tidak
# mengembalikan nilai.
# - Cetak kalimat sambutan hangat yang menyertakan nama mahasiswa
# menggunakan f-string.


def sapa_mahasiswa(nama):
    print(f"Halo {nama}, selamat datang di portal akademik!")


sapa_mahasiswa("Alfian")
