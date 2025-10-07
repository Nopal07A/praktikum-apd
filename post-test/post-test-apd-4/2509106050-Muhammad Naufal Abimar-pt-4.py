print("===== PROGRAM LOGIN =====")
while True:
    username = input("Username: ")
    password = input("Password: ")

    if username == "nopal" and password == "050":
        print("Login Berhasil!")
        print("Selamat datang", username)
        break
    elif username != "nopal" and password != "050":
        print("Username dan Password salah! Silakan coba lagi.")
    elif username != "nopal":
        print("Hanya username yang salah! Silakan coba lagi.")
    else:
        print("Username atau Password salah!")
        print("Coba lagi")

total_A_plus = 0
total_A_minus = 0
total_B_plus = 0
total_B_minus = 0
total_AB_plus = 0
total_AB_minus = 0
total_O_plus = 0
total_O_minus = 0

print("===== PROGRAM INPUT GOLONGAN DARAH =====")

while True:
    print("\n--- Input Data Donor ---")
    golongan = input("Masukkan golongan darah (A/B/AB/O): ").upper()
    
    if golongan == "A":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "+":
            kantong = int(input("Jumlah kantong darah: "))
            ml = kantong * 500
            total_A_plus = total_A_plus + ml
            print(f"Berhasil input {kantong} kantong darah A+ ({ml} ml)")
        elif rhesus == "-":
            kantong = int(input("Jumlah kantong darah: "))
            ml = kantong * 500
            total_A_minus = total_A_minus + ml
            print(f"Berhasil input {kantong} kantong darah A- ({ml} ml)")
    
    elif golongan == "B":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "+":
            kantong = int(input("Jumlah kantong darah: "))
            ml = kantong * 500
            total_B_plus = total_B_plus + ml
            print(f"Berhasil input {kantong} kantong darah B+ ({ml} ml)")
        elif rhesus == "-":
            kantong = int(input("Jumlah kantong darah: "))
            ml = kantong * 500
            total_B_minus = total_B_minus + ml
            print(f"Berhasil input {kantong} kantong darah B- ({ml} ml)")
    
    elif golongan == "AB":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "+":
            kantong = int(input("Jumlah kantong darah: "))
            ml = kantong * 500
            total_AB_plus = total_AB_plus + ml
            print(f"Berhasil input {kantong} kantong darah AB+ ({ml} ml)")
        elif rhesus == "-":
            kantong = int(input("Jumlah kantong darah: "))
            ml = kantong * 500
            total_AB_minus = total_AB_minus + ml
            print(f"Berhasil input {kantong} kantong darah AB- ({ml} ml)")
    
    elif golongan == "O":
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "+":
            kantong = int(input("Jumlah kantong darah: "))
            ml = kantong * 500
            total_O_plus = total_O_plus + ml
            print(f"Berhasil input {kantong} kantong darah O+ ({ml} ml)")
        elif rhesus == "-":
            kantong = int(input("Jumlah kantong darah: "))
            ml = kantong * 500
            total_O_minus = total_O_minus + ml
            print(f"Berhasil input {kantong} kantong darah O- ({ml} ml)")
    
    else:
        print("Golongan darah tidak valid!")
    
    
    lanjut = input("\nApakah anda masih mau input lagi (Y/T)? ").upper()
    if lanjut == "T":
        break


print("\n===== TOTAL JUMLAH DARAH =====")
print(f"Golongan A+  : {total_A_plus} ml")
print(f"Golongan A-  : {total_A_minus} ml")
print(f"Golongan B+  : {total_B_plus} ml")
print(f"Golongan B-  : {total_B_minus} ml")
print(f"Golongan AB+ : {total_AB_plus} ml")
print(f"Golongan AB- : {total_AB_minus} ml")
print(f"Golongan O+  : {total_O_plus} ml")
print(f"Golongan O-  : {total_O_minus} ml")
print("=" * 35)
total_semua = total_A_plus + total_A_minus + total_B_plus + total_B_minus + total_AB_plus + total_AB_minus + total_O_plus + total_O_minus
print(f"TOTAL SEMUA  : {total_semua} ml")