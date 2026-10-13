# CHALLENGE - Program Konversi Suhu Berulang
# Program menyediakan menu konversi suhu Fahrenheit dan Celsius menggunakan perulangan while True.

while True:
    print("\n1. Konversi Fahreinheit ke Celcius")
    print("2. Konversi Celcius ke Fahreinheit")
    print("3. Keluar")

    menu = input("Masukan menu [1-3] : ")

    # Pilihan 1: Konversi Fahrenheit ke Celsius dengan rumus (Fahrenheit - 32) * 5 / 9.
    if menu == "1":
        fahrenheit = float(input("\nMasukan suhu fahrenheit : "))

        celcius = (fahrenheit - 32) * 5 / 9
        print(f"Suhu dalam celcius adalah {celcius}")

    # Pilihan 2: Konversi Celsius ke Fahrenheit dengan rumus (Celsius * 9 / 5) + 32.
    elif menu == "2":
        celcius = float(input("\nMasukan suhu celcius : "))

        fahrenheit = (celcius * 9 / 5) + 32
        print(f"Suhu dalam fahrenheit adalah {fahrenheit}")

    # Pilihan 3: Hentikan perulangan untuk keluar dari program.
    elif menu == "3":
        break

    # Tampilkan pesan jika input tidak valid.
    else:
        print("Input tidak valid")