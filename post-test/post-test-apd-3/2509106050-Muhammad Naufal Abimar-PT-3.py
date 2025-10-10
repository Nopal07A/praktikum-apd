username = "nopal"
Password = "050"

ussername = input("masukkan ussername anda:")
password  = input("masukkan password anda:")

if ussername == username and password == Password:
    print("login berhasil")
elif username == ussername and Password != password:
    print("password anda salah")
    exit()
elif username != ussername and Password == password:
    print("username anda salah")
    exit()
else:
    print ("login gagal cek username dan password anda")
    exit()


print("=== Program Konversi ===")
print("1. konversi Panjang")
print("2. konversi Massa")
print("3. konversi Suhu")
print("4. konversi Waktu")
print("5. konversi mata uang")

konversi = input("Pilih konversi yang di inginkan (1-5): ")

if konversi == "1":
    print("--- Konversi Panjang ---")
    print("a. Feet -> Meter")
    print("b. Kilometer -> Meter")
    print("c. Centimeter -> Meter")
    pilihan = input("Pilih konversi (a - c): ")

    if pilihan == "a":
        nilai = float(input("Masukkan nilai (feet): "))
        hasil = nilai * 0.3048
        print(nilai, "feet =", hasil, "meter")
    elif pilihan == "b":
        nilai = float(input("Masukkan nilai (km): "))
        hasil = nilai * 1000
        print(nilai, "km =", hasil, "meter")
    elif pilihan == "c":
        nilai = float(input("Masukkan nilai (cm): "))
        hasil = nilai / 100
        print(nilai, "cm =", hasil, "meter")
    else:
        print("Pilihan tidak ada.")

elif konversi == "2":
    print("--- Konversi Massa ---")
    print("a. Pound -> Kilogram")
    print("b. Ton -> Kilogram")
    print("c. Gram -> Kilogram")
    print("d. hektogram -> kilogram")
    print("e. dekagram -> kilogram")
    pilihan = input("Pilih konversi (a - e): ")

    if pilihan == "a":
        nilai = float(input("Masukkan nilai (pound): "))
        hasil = nilai * 2.2
        print(nilai, "pound =", hasil, "kg")
    elif pilihan == "b":
        nilai = float(input("Masukkan nilai (ton): "))
        hasil = nilai * 1000
        print(nilai, "ton =", hasil, "kg")
    elif pilihan == "c":
        nilai = float(input("Masukkan nilai (gram): "))
        hasil = nilai / 1000
        print(nilai, "gram =", hasil, "kg")
    elif pilihan == "d":
        nilai = float(input("masukkan nilai hektogram (hg)"))
        hasil = nilai / 10
        print(nilai, "hg=", hasil, "kg")
    elif pilihan == "e":
        nilai = float(input("masukkan nilai dekagram (dag)"))
        hasil = nilai / 100
        print(nilai, "dag=", hasil, "kg")
    else:
        print("Pilihan tidak ada.")

elif konversi == "3":
    print("--- Konversi Suhu ---")
    print("a. Celcius -> Kelvin")
    print("b. Fahrenheit -> Kelvin")
    print("c. Reamur -> Kelvin")
    pilihan = input("Pilih konversi (a - c): ")

    if pilihan == "a":
        nilai = float(input("Masukkan suhu (C): "))
        hasil = nilai + 273.15
        print(nilai, "°C =", hasil, "K")
    elif pilihan == "b":
        nilai = float(input("Masukkan suhu (F): "))
        hasil = (nilai - 32) * 5/9 + 273.15
        print(nilai, "F =", hasil, "K")
    elif pilihan == "c":
        nilai = float(input("Masukkan suhu (R): "))
        hasil = nilai * 5/4 + 273.15
        print(nilai, "R =", hasil, "K")
    else:
        print("Pilihan tidak ada.")

elif konversi == "4":
    print("--- Konversi Waktu ---")
    print("a. Menit -> Detik")
    print("b. Jam -> Detik")
    pilihan = input("Pilih konversi (a-b): ")

    if pilihan == "a":
        nilai = float(input("Masukkan nilai (menit): "))
        hasil = nilai * 60
        print(nilai, "menit =", hasil, "detik")
    elif pilihan == "b":
        nilai = float(input("Masukkan nilai (jam): "))
        hasil = nilai * 3600
        print(nilai, "jam =", hasil, "detik")
    else:
        print("Pilihan tidak ada.")

elif konversi == "5":
    print("--- Konversi Mata Uang ---")
    print("a. Rupiah -> Dolar (USD)")
    print("b. Dolar (USD) -> Rupiah")
    print("c. Rupiah -> Yen (JPY)")
    print("d. Yen (JPY) -> Rupiah")
    print("e. Rupiah -> Won (KRW)")
    print("f. Won (KRW) -> Rupiah")
    pilihan = input("Pilih konversi (a-f): ")

    if pilihan == "a":
        nilai = float(input("Masukkan nilai (Rp): "))
        hasil = nilai / 16703
        print( nilai, "Rp= ", hasil, "USD")
    elif pilihan == "b":
        nilai = float(input("Masukkan nilai (USD): "))
        hasil = nilai * 16703
        print(nilai, "USD = ", hasil, "rp")
    elif pilihan == "c":
        nilai = float(input("Masukkan nilai (Rp): "))
        hasil = nilai / 111.56
        print(nilai, "Rp = ", hasil, "JPY")
    elif pilihan == "d":
        nilai = float(input("Masukkan nilai (JPY): "))
        hasil = nilai * 111.56
        print(nilai, "JPY = ", hasil, "rp")
    elif pilihan == "e":
        nilai = float(input("Masukkan nilai (Rp): "))
        hasil = nilai / 11.83
        print(nilai, "rp = ", hasil, "KRW")
    elif pilihan == "f":
        nilai = float(input("Masukkan nilai (KRW): "))
        hasil = nilai * 11.83
        print(nilai, "KRW = ", hasil, "rp")
    else:
        print("Pilihan tidak ada.")

else:
    print("Kategori tidak ada.")





