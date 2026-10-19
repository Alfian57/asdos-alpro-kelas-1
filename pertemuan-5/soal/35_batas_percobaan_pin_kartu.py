# Soal 35: Batas Percobaan PIN Kartu
# Cerita: Mesin transaksi memberikan kesempatan maksimal 3 kali kepada pengguna
# untuk memasukkan PIN yang benar sebelum sistem terkunci.
# Spesifikasi:
# - Inisialisasi variabel percobaan = 1.
# - Gunakan while percobaan <= 3 untuk meminta input PIN teks dari pengguna.
# - Jika PIN bernilai "9999", tampilkan pesan sukses dan keluar dengan break.
# - Jika salah dan percobaan mencapai 3, tampilkan pesan "Kartu diblokir".
# - Tingkatkan nilai percobaan setiap kali tebakan salah.


percobaan = 1

while percobaan <= 3:
    pin = input("Masukan PIN: ")
    if pin == "9999":
        print("Sukses, PIN benar!")
        break
    else:
        if percobaan == 3:
            print("Kartu diblokir")
        else:
            print("PIN salah.")
        percobaan += 1
