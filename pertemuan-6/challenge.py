list_nama = ["fahmi", "raja"]

def cetak_menu():
    print("\n=========================")
    print("Program Management Antrean")
    print("=========================")
    print("1. Lihat antrean")
    print("2. Tambah antrean")
    print("3. Hapus antrean")
    print("4. Keluar")

while True:
    cetak_menu()
    menu = input("Masukan menu [1-4] : ")

    if menu == "1":
        for nama in list_nama:
            print(f"Nama {nama}")

    elif menu == "2":
        nama = input("\nMasukan nama orang: ")
        list_nama.append(nama)

    elif menu == "3":
        nama = input("\nMasukan nama orang: ")
        list_nama.remove(nama)

    elif menu == "4":
        break

    else:
        print("\n================")
        print("Menu tidak valid")
        print("================")