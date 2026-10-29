# Soal 80: Program Manajemen Inventaris Alat Laboratorium
# Cerita: Kepala laboratorium komputer membutuhkan program manajemen inventaris berbasis
# menu untuk melihat daftar alat, menambah alat baru, dan menghapus alat yang dipindahkan.
# Spesifikasi:
# - Buat list list_alat = ["proyektor", "kabel"] dan fungsi cetak_menu() yang mencetak
# judul serta menu 1 sampai 4.
# - Gunakan perulangan while True untuk memanggil cetak_menu() dan meminta input
# pilihan pengguna.
# - Jika "1" tampilkan seluruh alat dengan for alat in list_alat:, jika "2" minta input alat
# baru lalu tambahkan dengan .append(), jika "3" minta input nama alat lalu hapus
# dengan .remove(), jika "4" jalankan break, dan jika input lain tampilkan "Menu tidak
# valid".


list_alat = ["proyektor", "kabel"]


def cetak_menu():
    print("\n=========================")
    print("Program Manajemen Inventaris Alat Laboratorium")
    print("=========================")
    print("1. Lihat alat")
    print("2. Tambah alat")
    print("3. Hapus alat")
    print("4. Keluar")


while True:
    cetak_menu()
    menu = input("Masukan menu [1-4] : ")

    if menu == "1":
        for alat in list_alat:
            print(alat)
    elif menu == "2":
        alat_baru = input("\nMasukan nama alat baru: ")
        list_alat.append(alat_baru)
    elif menu == "3":
        nama_alat = input("\nMasukan nama alat yang dihapus: ")
        list_alat.remove(nama_alat)
    elif menu == "4":
        break
    else:
        print("\n================")
        print("Menu tidak valid")
        print("================")
