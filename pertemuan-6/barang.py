list_barang = ["radio", "kertas"]

def cetak_menu():
    print("\n=========================")
    print("Program Management Barang")
    print("=========================")
    print("1. Lihat barang")
    print("2. Tambah barang")
    print("3. Hapus barang")
    print("4. Keluar")

while True:
    cetak_menu()
    menu = input("Masukan menu [1-4] : ")

    if menu == "1":
        for barang in list_barang:
            print(f"Barang {barang}")

    elif menu == "2":
        nama_barang = input("\nMasukan nama barang: ")
        list_barang.append(nama_barang)

    elif menu == "3":
        nama_barang = input("\nMasukan nama barang: ")
        list_barang.remove(nama_barang)

    elif menu == "4":
        break

    else:
        print("\n================")
        print("Menu tidak valid")
        print("================")