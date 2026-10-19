# Soal 59: Penentuan Status Kelulusan Nilai
# Cerita: Bagian kurikulum membutuhkan fungsi logika untuk mengevaluasi apakah
# seorang siswa berhak lulus berdasarkan batas nilai minimal 75.
# Spesifikasi:
# - Buat fungsi dengan return cek_kelulusan(nilai).
# - Menerima parameter nilai bertipe float atau integer.
# - Jika nilai >= 75, kembalikan string "LULUS".
# - Jika nilai < 75, kembalikan string "TIDAK LULUS".


def cek_kelulusan(nilai):
    if nilai >= 75:
        return "LULUS"
    else:
        return "TIDAK LULUS"


status = cek_kelulusan(80)
print(f"Status kelulusan: {status}")
