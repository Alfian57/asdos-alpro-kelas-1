# Program mendemonstrasikan fungsi tanpa parameter.
# Fungsi mengelompokkan serangkaian instruksi persiapan ke kampus agar dapat dipanggil berulang kali tanpa menulis ulang kode.

# Mendefinisikan fungsi persiapan_berangkat_ke_kampus tanpa parameter.
def persiapan_berangkat_ke_kampus():
    # Menampilkan urutan langkah-langkah persiapan sebelum berangkat ke kampus.
    print("Bangun pagi dan merapikan tempat tidur")
    print("Mandi pagi dan menggosok gigi")
    print("Mengenakan pakaian rapi untuk kuliah")
    print("Sarapan pagi")
    print("Menyiapkan buku dan berangkat ke kampus")


# Memanggil fungsi pada hari Senin.
print("Senin")
persiapan_berangkat_ke_kampus()

# Memanggil kembali fungsi yang sama pada hari Selasa.
print("\nSelasa")
persiapan_berangkat_ke_kampus()

# Memanggil kembali fungsi yang sama pada hari Rabu.
print("\nRabu")
persiapan_berangkat_ke_kampus()