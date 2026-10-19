# CHALLENGE - Soal 60: Hitung Biaya Sewa Lapangan Futsal
# Cerita: Pengelola gedung olahraga menerapkan tarif sewa lapangan futsal berdasarkan jumlah jam sewa dan tarif dasar per jamnya.
# Spesifikasi:
# Buat fungsi dengan return hitung_sewa_lapangan(durasi_jam, tarif_per_jam).
# Menerima dua parameter integer: durasi_jam dan tarif_per_jam.
# Hitung total biaya dengan mengalikan kedua parameter tersebut.
# Kembalikan (return) total biaya sewa yang didapat.

# Mendefinisikan fungsi hitung_sewa_lapangan dengan dua parameter durasi dan tarif per jam.
def hitung_sewa_lapangan(durasi_jam, tarif_per_jam):
    # Hitung total biaya dengan mengalikan durasi jam dengan tarif per jam.
    total_biaya = durasi_jam * tarif_per_jam
    # Mengembalikan nilai total biaya sewa ke pemanggil fungsi.
    return total_biaya


# Contoh pengujian fungsi: memanggil fungsi dengan durasi 2 jam dan tarif Rp 100.000 per jam.
biaya = hitung_sewa_lapangan(2, 100000)

# Menampilkan hasil perhitungan biaya sewa lapangan ke layar.
print(f"Total biaya sewa lapangan: Rp {biaya}")
