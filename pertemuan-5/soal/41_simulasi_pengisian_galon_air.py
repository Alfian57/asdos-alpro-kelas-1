# Soal 41: Simulasi Pengisian Galon Air
# Cerita: Sebuah galon air berkapasitas 19 liter diisi air dari kran dengan laju
# penambahan 2 liter setiap detik simulasi.
# Spesifikasi:
# - Inisialisasi variabel isi_air = 0 dan detik = 0.
# - Gunakan while isi_air < 19.
# - Tambahkan 2 pada isi_air dan 1 pada detik.
# - Tampilkan volume air pada detik berjalan menggunakan f-string.
# - Jika volume melebihi atau sama dengan 19, tampilkan "Galon penuh".


isi_air = 0
detik = 0

while isi_air < 19:
    isi_air += 2
    detik += 1
    print(f"Detik ke-{detik}: volume air = {isi_air} liter")
    if isi_air >= 19:
        print("Galon penuh")
