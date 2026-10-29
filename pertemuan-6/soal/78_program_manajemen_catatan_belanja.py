# Soal 78: Program Manajemen Catatan Belanja
# Cerita: Ibu rumah tangga membutuhkan program menu berulang sederhana untuk melihat
# daftar belanjaan dan menambahkan barang belanjaan baru sebelum pergi ke pasar.
# Spesifikasi:
# - Buat list awal daftar_belanja = ["beras", "telur"].
# - Gunakan while True untuk menampilkan pilihan menu: "1" Lihat belanjaan, "2"
# Tambah belanjaan, dan "3" Keluar.
# - Jika pilih "1", tampilkan seluruh isi daftar_belanja menggunakan perulangan for.
# - Jika pilih "2", minta input nama barang dan tambahkan ke list menggunakan
# .append().
# - Jika pilih "3", hentikan perulangan menggunakan break.


daftar_belanja = ["beras", "telur"]

while True:
    print("\n--- Program Catatan Belanja ---")
    print("1. Lihat belanjaan")
    print("2. Tambah belanjaan")
    print("3. Keluar")
    menu = input("Pilih menu [1/2/3]: ")

    if menu == "1":
        for barang in daftar_belanja:
            print(barang)
    elif menu == "2":
        barang = input("Masukan nama barang: ")
        daftar_belanja.append(barang)
    elif menu == "3":
        break
    else:
        print("Menu tidak valid")
