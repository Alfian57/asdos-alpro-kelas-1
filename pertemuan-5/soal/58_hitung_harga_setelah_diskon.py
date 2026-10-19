# Soal 58: Hitung Harga Setelah Diskon
# Cerita: Kasir toko pakaian memerlukan fungsi matematika yang menghitung harga
# bersih suatu barang setelah dipotong persentase diskon.
# Spesifikasi:
# - Buat fungsi dengan return hitung_harga_diskon(harga_asli, persen_diskon).
# - Menerima parameter harga_asli (int/float) dan persen_diskon (float dalam
# desimal, misal 0.2 untuk 20%).
# - Hitung potongan harga (harga_asli * persen_diskon), lalu kurangkan dari
# harga_asli.
# - Kembalikan (return) harga akhir setelah diskon.


def hitung_harga_diskon(harga_asli, persen_diskon):
    potongan_harga = harga_asli * persen_diskon
    harga_akhir = harga_asli - potongan_harga
    return harga_akhir


hasil = hitung_harga_diskon(100000, 0.2)
print(f"Harga setelah diskon: Rp{hasil}")
