# Program kasir sederhana yang menjumlahkan harga barang belanjaan.
# Menggunakan while True untuk terus menampilkan menu sampai pengguna memilih keluar.

# Variabel penyimpan total belanja yang dimulai dari 0.
total_harga = 0

# Perulangan terus berjalan sampai perintah break dijalankan.
while True:
    print("\n1. Tambah barang")
    print("2. Keluar")
    menu = input("Masukan menu [1-2] : ")

    # Tambah harga barang ke total belanja.
    if menu == "1":
        harga = int(input("Masukan harga : "))
        total_harga = total_harga + harga

    # Tampilkan total harga belanjaan lalu hentikan perulangan dengan break.
    elif menu == "2":
        print(f"\nTotal Harga adalah {total_harga}")
        break

    # Tampilkan pesan jika pilihan menu tidak valid.
    else:
        print("\nInput tidak valid")