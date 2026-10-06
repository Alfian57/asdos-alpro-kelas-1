# Percabangan memilih tindakan berdasarkan kondisi.
# if memeriksa kondisi pertama; jika True, blok kodenya dijalankan dan sisanya dilewati.
# elif memeriksa kondisi berikutnya hanya jika semua kondisi sebelumnya False.
# else dijalankan jika tidak ada kondisi yang terpenuhi.
# Urutan kondisi penting: kondisi yang lebih spesifik harus ditulis lebih dulu.
nilai = 20

# Periksa apakah nilai lebih dari 80; jika ya, cetak "A" dan lewati elif dan else.
if nilai > 80:
    print("Nilai nya adalah A")
# Jika kondisi if False, periksa apakah nilai lebih dari 60.
elif nilai > 60:
    print("Nilai nya adalah B")
# Jika semua kondisi di atas False, periksa apakah nilai lebih dari 40.
elif nilai > 40:
    print("Nilai nya adalah C")
# Jika tidak ada kondisi yang terpenuhi, jalankan else; nilai 20 masuk ke sini.
else:
    print("Nilai nya adalah D")
