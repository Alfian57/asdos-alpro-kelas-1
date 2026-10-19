# Soal 44: Menu Layanan Mandiri Bank
# Cerita: Mesin antrean bank menampilkan menu interaktif pilihan layanan (1: Setor
# Tunai, 2: Informasi Saldo, 3: Selesai) yang akan terus muncul sampai nasabah
# memilih nomor 3.
# Spesifikasi:
# - Gunakan while True.
# - Cetak pilihan menu 1, 2, dan 3, kemudian minta input menu dari pengguna.
# - Jika menu "1", cetak keterangan layanan setor tunai.
# - Jika menu "2", cetak keterangan informasi saldo.
# - Jika menu "3", cetak ucapan terima kasih dan keluar menggunakan break.
# - Jika pilihan lain, cetak "Pilihan tidak valid".


while True:
    print("\n--- Menu Layanan Mandiri Bank ---")
    print("1: Setor Tunai")
    print("2: Informasi Saldo")
    print("3: Selesai")
    menu = input("Pilih menu [1/2/3]: ")

    if menu == "1":
        print("Layanan Setor Tunai: Silakan masukkan uang Anda.")
    elif menu == "2":
        print("Layanan Informasi Saldo: Saldo Anda mencukupi.")
    elif menu == "3":
        print("Terima kasih telah menggunakan layanan kami.")
        break
    else:
        print("Pilihan tidak valid")
