# Soal 25: Validasi Penarikan Tunai ATM
# Cerita: Nasabah ingin menarik uang tunai dari ATM. Saldo rekening saat ini adalah
# Rp500.000. Penarikan hanya dapat diproses jika nominal yang ditarik tidak melebihi
# saldo.
# Spesifikasi:
# - Tetapkan variabel saldo = 500000.
# - Minta input nominal penarikan (int) ke dalam variabel tarik.
# - Jika tarik <= saldo, hitung sisa saldo dan tampilkan pesan transaksi berhasil
# beserta sisa saldo.
# - Jika tarik > saldo, tampilkan pesan "Saldo tidak mencukupi".


saldo = 500000
tarik = int(input("Masukan nominal penarikan: "))

if tarik <= saldo:
    saldo -= tarik
    print(f"Transaksi berhasil. Sisa saldo Anda: Rp{saldo}")
else:
    print("Saldo tidak mencukupi")
