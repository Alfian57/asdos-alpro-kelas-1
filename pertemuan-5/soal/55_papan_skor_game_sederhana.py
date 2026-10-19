# Soal 55: Papan Skor Game Sederhana
# Cerita: Pengembang game konsol teks ingin menampilkan papan skor sementara
# pemain setiap kali menyelesaikan sebuah ronde.
# Spesifikasi:
# - Buat fungsi dengan parameter tampilkan_skor(nama_pemain, poin).
# - Menerima parameter nama_pemain (string) dan poin (integer), tanpa return.
# - Tampilkan nama pemain beserta total poin yang diraihnya.


def tampilkan_skor(nama_pemain, poin):
    print(f"Pemain: {nama_pemain} | Skor: {poin} poin")


tampilkan_skor("Player1", 100)
