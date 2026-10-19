# Program autentikasi login sederhana menggunakan fungsi dan perulangan.
# Fungsi login mengembalikan nilai boolean (True/False) untuk menentukan apakah login berhasil.
# Perulangan while True digunakan agar pengguna terus diminta input hingga berhasil login.

# Fungsi untuk memverifikasi kecocokan NIM dan password yang dimasukkan.
def login(nim, password):
    # Operator and memastikan kedua kondisi harus bernilai benar.
    if nim == "5230411121" and password == "rahasia123":
        return True
    else:
        return False


# Perulangan berjalan terus menerus sampai login berhasil dan perintah break dieksekusi.
while True:
    input_nim = input("Masukan nim : ")
    input_password = input("Masukan password : ")

    # Memanggil fungsi login dengan argumen yang diinputkan pengguna.
    login_berhasil = login(input_nim, input_password)

    # Jika login bernilai True, tampilkan pesan sukses dan hentikan perulangan.
    if login_berhasil:
        print("Login berhasil")
        break
    # Jika login bernilai False, tampilkan pesan kegagalan dan ulangi perulangan.
    else:
        print("Login gagal")