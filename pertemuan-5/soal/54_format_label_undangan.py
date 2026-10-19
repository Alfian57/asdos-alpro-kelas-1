# Soal 54: Format Label Undangan
# Cerita: Panitia seminar mencetak label tamu undangan yang berisi nama tamu dan
# instansi asalnya.
# Spesifikasi:
# - Buat fungsi dengan parameter cetak_undangan(nama_tamu, instansi).
# - Menerima 2 parameter bertipe string tanpa mengembalikan nilai.
# - Tampilkan format kartu undangan dengan garis pembatas di atas dan
# bawahnya.


def cetak_undangan(nama_tamu, instansi):
    print("=" * 40)
    print(f"Kepada Yth: {nama_tamu}")
    print(f"Instansi  : {instansi}")
    print("=" * 40)


cetak_undangan("Budi Santoso", "Universitas Indonesia")
