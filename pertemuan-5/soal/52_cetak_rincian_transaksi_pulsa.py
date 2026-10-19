# Soal 52: Cetak Rincian Transaksi Pulsa
# Cerita: Konter pulsa membutuhkan fungsi untuk mencetak ringkasan transaksi
# setelah pembeli memilih nominal pulsa.
# Spesifikasi:
# - Buat fungsi dengan parameter cetak_transaksi(nomor_hp, nominal).
# - Fungsi menerima 2 parameter: nomor_hp (string) dan nominal (integer), tanpa
# return.
# - Tampilkan format rincian nomor tujuan dan nominal pulsa ke layar.


def cetak_transaksi(nomor_hp, nominal):
    print("--- Rincian Transaksi Pulsa ---")
    print(f"Nomor Tujuan  : {nomor_hp}")
    print(f"Nominal Pulsa : Rp{nominal}")


cetak_transaksi("081234567890", 50000)
