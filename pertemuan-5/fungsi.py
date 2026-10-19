# Fungsi (function) adalah blok kode terorganisir yang dibuat untuk melakukan tugas tertentu.
# Dengan fungsi, sekumpulan kode dapat digunakan kembali (reusable) tanpa perlu menulis ulang instruksi yang sama.
# def digunakan untuk mendefinisikan sebuah fungsi baru dalam Python.

# Mendefinisikan fungsi bernama memasak_telur tanpa parameter.
def memasak_telur():
    # Menampilkan langkah-langkah proses memasak telur.
    print("Memasukan minyak")
    print("Memasukan telur")
    print("Memasukan garam")
    print("Angkat telur")
    print("Hidangkan telur")


# Memanggil fungsi memasak_telur pada hari Senin.
print("Senin")
memasak_telur()

# Memanggil kembali fungsi memasak_telur pada hari Rabu.
print("\nRabu")
memasak_telur()

# Memanggil kembali fungsi memasak_telur pada hari Minggu.
print("\nMinggu")
memasak_telur()
