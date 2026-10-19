# Soal 53: Notifikasi Pengingat Rapat
# Cerita: Aplikasi kalender sekretariat membutuhkan fungsi cetak pengingat agenda
# pertemuan bagi pengurus organisasi.
# Spesifikasi:
# - Buat fungsi dengan parameter ingatkan_agenda(nama_agenda, jam).
# - Fungsi menerima parameter nama_agenda (string) dan jam (string), tanpa
# return.
# - Tampilkan pesan pengingat agenda beserta jam pelaksanaannya menggunakan
# f-string.


def ingatkan_agenda(nama_agenda, jam):
    print(f"Pengingat: Agenda '{nama_agenda}' akan dimulai pada pukul {jam}.")


ingatkan_agenda("Rapat Koordinasi", "14:00")
