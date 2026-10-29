# Soal 74: Fungsi Cetak Daftar Hadir Mahasiswa
# Cerita: Pengajar ingin membungkus proses penampilan daftar nama mahasiswa yang hadir ke
# dalam sebuah fungsi agar mudah dipanggil kapan saja.
# Spesifikasi:
# - Buat list daftar_hadir = ["fahmi", "raja", "shabrina"].
# - Buat fungsi biasa cetak_kehadiran() tanpa parameter dan tanpa return.
# - Di dalam fungsi, gunakan perulangan for nama in daftar_hadir: untuk mencetak setiap
# nama mahasiswa.
# - Panggil fungsi cetak_kehadiran().


daftar_hadir = ["fahmi", "raja", "shabrina"]


def cetak_kehadiran():
    for nama in daftar_hadir:
        print(nama)


cetak_kehadiran()
