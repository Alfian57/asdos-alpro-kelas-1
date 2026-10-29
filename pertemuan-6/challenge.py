# CHALLENGE - Program Manajemen Antrean
# Program simulasi pengelolaan antrean menggunakan list, fungsi, dan perulangan while True.

# Inisialisasi list awal yang berisi nama dalam antrean.
list_nama = ["fahmi", "raja"]


# Fungsi untuk menampilkan daftar menu antrean.
def cetak_menu():
    print("\n=========================")
    print("Program Management Antrean")
    print("=========================")
    print("1. Lihat antrean")
    print("2. Tambah antrean")
    print("3. Hapus antrean")
    print("4. Keluar")


# Perulangan utama program berjalan hingga pengguna memilih keluar.
while True:
    cetak_menu()
    menu = input("Masukan menu [1-4] : ")

    # Menu 1: Menampilkan seluruh nama dalam antrean menggunakan perulangan for.
    if menu == "1":
        for nama in list_nama:
            print(f"Nama {nama}")

    # Menu 2: Menambahkan nama orang ke antrean menggunakan append().
    elif menu == "2":
        nama = input("\nMasukan nama orang: ")
        list_nama.append(nama)

    # Menu 3: Menghapus nama orang dari antrean menggunakan remove().
    elif menu == "3":
        nama = input("\nMasukan nama orang: ")
        list_nama.remove(nama)

    # Menu 4: Menghentikan perulangan untuk keluar dari program.
    elif menu == "4":
        break

    # Menampilkan pesan jika pilihan menu tidak valid.
    else:
        print("\n================")
        print("Menu tidak valid")
        print("================")
