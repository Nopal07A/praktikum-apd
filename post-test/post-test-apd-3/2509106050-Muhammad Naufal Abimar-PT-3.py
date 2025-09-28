username = "nopal"
Password = "050"

ussername = input("masukkan ussername anda:")
password  = input("masukkan password anda:")

if ussername == username and password == Password:
    print("login berhasil")
elif username == ussername and Password != password:
    print("password anda salah")
elif username != ussername and Password == password:
    print("username anda salah")
else:
    print ("login gagal cek username dan password anda")


