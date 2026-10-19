# Soal 60: Hitung Biaya Sewa Lapangan Futsal
# Cerita: Pengelola gedung olahraga menerapkan tarif sewa lapangan futsal
# berdasarkan jumlah jam sewa dan tarif dasar per jamnya.
# Spesifikasi:
# - Buat fungsi dengan return hitung_sewa_lapangan(durasi_jam, tarif_per_jam).
# - Menerima dua parameter integer: durasi_jam dan tarif_per_jam.
# - Hitung total biaya dengan mengalikan kedua parameter tersebut.
# - Kembalikan (return) total biaya sewa yang didapat.


def hitung_sewa_lapangan(durasi_jam, tarif_per_jam):
    total_biaya = durasi_jam * tarif_per_jam
    return total_biaya


biaya = hitung_sewa_lapangan(2, 100000)
print(f"Total biaya sewa: Rp{biaya}")
