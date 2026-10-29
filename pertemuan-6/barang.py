# Program manajemen barang sederhana menggunakan list dan fungsi.
# Program menyediakan menu interaktif untuk mengelola data barang secara berulang.

# Inisialisasi list penampung data barang.
list_barang = ["radio", "kertas"]


# Fungsi untuk menampilkan daftar menu pilihan program.
def cetak_menu():
    print("\n=========================")
    print("Program Management Barang")
    print("=========================")
    print("1. Lihat barang")
    print("2. Tambah barang")
    print("3. Hapus barang")
    print("4. Keluar")


# Perulangan utama program berjalan hingga pengguna memilih keluar.
while True:
    cetak_menu()
    menu = input("Masukan menu [1-4] : ")

    # Menu 1: Menampilkan seluruh data barang menggunakan perulangan for.
    if menu == "1":
        for barang in list_barang:
            print(f"Barang {barang}")

    # Menu 2: Menambahkan barang baru ke dalam list menggunakan append().
    elif menu == "2":
        nama_barang = input("\nMasukan nama barang: ")
        list_barang.append(nama_barang)

    # Menu 3: Menghapus data barang dari list berdasarkan input menggunakan remove().
    elif menu == "3":
        nama_barang = input("\nMasukan nama barang: ")
        list_barang.remove(nama_barang)

    # Menu 4: Menghentikan perulangan untuk keluar dari program.
    elif menu == "4":
        break

    # Menampilkan pesan jika pilihan menu tidak valid.
    else:
        print("\n================")
        print("Menu tidak valid")
        print("================")
