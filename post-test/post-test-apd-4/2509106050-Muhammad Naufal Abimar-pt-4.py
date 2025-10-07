print("===== PROGRAM LOGIN =====")
while True:
    username = input("Username: ")
    password = input("Password: ")

    if username == "nopal" and password == "050":
        print("Login Berhasil!")
        print("Selamat datang", username)
        break
    else:
        print("Username atau Password salah!")
        print("Coba lagi")