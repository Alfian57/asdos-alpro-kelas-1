# Soal 79: Program Manajemen Antrean Servis Motor
# Cerita: Bengkel motor membutuhkan aplikasi terminal untuk mencatat antrean pelanggan
# yang datang servis, melihat antrean saat ini, serta menghapus nama pelanggan yang sudah
# selesai dilayani.
# Spesifikasi:
# - Buat list list_antrean = ["fahmi", "raja"] dan fungsi cetak_menu() untuk menampilkan
# 4 pilihan menu.
# - Gunakan while True untuk meminta input menu "1" sampai "4".
# - Menu "1" menampilkan setiap nama di list_antrean dengan perulangan for, menu "2"
# menambah nama dengan .append(), menu "3" menghapus nama dengan .remove(),
# menu "4" keluar dengan break, dan selain itu mencetak "Menu tidak valid".


list_antrean = ["fahmi", "raja"]


def cetak_menu():
    print("\n=========================")
    print("Program Manajemen Antrean Servis Motor")
    print("=========================")
    print("1. Lihat antrean")
    print("2. Tambah antrean")
    print("3. Hapus antrean")
    print("4. Keluar")


while True:
    cetak_menu()
    menu = input("Masukan menu [1-4] : ")

    if menu == "1":
        for nama in list_antrean:
            print(nama)
    elif menu == "2":
        nama = input("\nMasukan nama pelanggan: ")
        list_antrean.append(nama)
    elif menu == "3":
        nama = input("\nMasukan nama pelanggan yang dihapus: ")
        list_antrean.remove(nama)
    elif menu == "4":
        break
    else:
        print("\n================")
        print("Menu tidak valid")
        print("================")
