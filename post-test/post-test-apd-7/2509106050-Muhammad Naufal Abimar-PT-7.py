import os
os.system('clear')

hero_meta = {
    "Mage": ["Yve", "Zhuxin", "Pharsa", "Zetian", "Novaria", "Kadita"],
    "Tank/Support": ["Floryn", "Mathilda", "Kalea", "Angela", "Badang", "Grock", "Gatot"],
    "Assassin": ["Hayabusa", "Fanny", "Yi_sun_shin", "Lancelot", "Fredrin"],
    "Fighter": ["Alice", "Cici", "Arlot", "Phoveus", "Gloo"],
    "Marksman": ["Granger", "Nathan", "Wanwan", "Obsidia"]
}

pengguna_baru = {}
username_admin = "admin"
password_admin = "admin123"

def cek_login(user, pw, tipe):
    if tipe == "user":
        if user in pengguna_baru and pengguna_baru[user] == pw:
            return True
        else:
            return False
    elif tipe == "admin":
        if user == username_admin and pw == password_admin:
            return True
        else:
            return False

def cari_hero(nama):
    for role in hero_meta:
        if nama in hero_meta[role]:
            return True, role
    return False, 

def hitung_hero():
    total = 0
    for role in hero_meta:
        total = total + len(hero_meta[role])
    return total

def tampilkan_statistik():
    print("\n" + "="*50)
    print("STATISTIK HERO")
    print("="*50)
    total = hitung_hero()
    print(f"Total Hero: {total}")
    print(f"Total Role: {len(hero_meta)}")
    print("\nJumlah per Role:")
    for role in hero_meta:
        print(f"  {role}: {len(hero_meta[role])} hero")
    print("="*50)

def tampilkan_hero():
    print("\n" + "="*50)
    print("DAFTAR HERO META")
    print("="*50)
    nomor = 1
    for role in hero_meta:
        print(f"\n{nomor}. {role}:")
        no_hero = 1
        for hero in hero_meta[role]:
            print(f"   {no_hero}. {hero}")
            no_hero = no_hero + 1
        nomor = nomor + 1
    print("="*50)

def daftar_user():
    print("\n=== DAFTAR USER BARU ===")
    user_baru = input("Username baru: ")
    
    if user_baru == "":
        print("Username tidak boleh kosong!")
        return
    
    if user_baru in pengguna_baru:
        print("Username sudah ada!")
        return
    
    pw_baru = input("Password baru: ")
    
    if pw_baru == "":
        print("Password tidak boleh kosong!")
        return
    
    if len(pw_baru) < 6:
        print("Password minimal 6 karakter!")
        return
    
    pengguna_baru[user_baru] = pw_baru
    print(f"User '{user_baru}' berhasil terdaftar!")

lanjut = True
while lanjut:
    try:
        print("\n" + "="*50)
        print("SISTEM MANAGEMENT HERO META")
        print("="*50)
        print("1. Daftar pengguna baru")
        print("2. Login sebagai user")
        print("3. Login sebagai admin")
        print("4. Keluar")
        print("="*50)
        pilih = input("Pilihan (1-4): ")
        
        if pilih == "1":
            daftar_user()
            
        elif pilih == "2":
            print("\n=== LOGIN USER ===")
            user_input = input("Username: ")
            pw_input = input("Password: ")
            
            login_sukses = cek_login(user_input, pw_input, "user")
            
            if login_sukses:
                print("\nLogin berhasil!")
                input("Tekan enter untuk melanjutkan...")
                
                menu_user = True
                while menu_user:
                    try:
                        print("\n" + "="*50)
                        print("MENU USER")
                        print("="*50)
                        print("1. Lihat daftar hero")
                        print("2. Cari hero")
                        print("3. Statistik")
                        print("4. Logout")
                        print("="*50)
                        pilih_user = input("Pilih (1-4): ")
                        
                        if pilih_user == "1":
                            tampilkan_hero()
                            input("\nTekan enter unutk melanjutkan...")
                            
                        elif pilih_user == "2":
                            nama_cari = input("\nNama hero: ")
                            ketemu, role = cari_hero(nama_cari)
                            if ketemu:
                                print(f"Hero '{nama_cari}' ada di role {role}")
                            else:
                                print(f"Hero '{nama_cari}' tidak ada")
                            input("\nTekan enter unutk melanjutkan...")
                            
                        elif pilih_user == "3":
                            tampilkan_statistik()
                            input("\nTekan enter unutk melanjutkan...")
                            
                        elif pilih_user == "4":
                            print("\nLogout berhasil!")
                            menu_user = False
                        else:
                            print("Pilihan salah!")
                    except:
                        print("Terjadi error!")
            else:
                print("\nLogin gagal!")
                
        elif pilih == "3":
            print("\n=== LOGIN ADMIN ===")
            user_input = input("Username: ")
            pw_input = input("Password: ")
            
            login_sukses = cek_login(user_input, pw_input, "admin")
            
            if login_sukses:
                print(f"\nSelamat datang, Admin!")
                input("Tekan enter unutk melanjutkan...")
                
                menu_admin = True
                while menu_admin:
                    try:
                        print("\n" + "="*50)
                        print("MENU ADMIN")
                        print("="*50)
                        print("1. Lihat daftar hero")
                        print("2. Tambah hero")
                        print("3. Hapus hero")
                        print("4. Cari hero")
                        print("5. Statistik")
                        print("6. Logout")
                        print("="*50)
                        pilih_admin = input("Pilih (1-6): ")
                        
                        if pilih_admin == "1":
                            tampilkan_hero()
                            input("\nTekan enter unutk melanjutkan...")
                            
                        elif pilih_admin == "2":
                            tampilkan_hero()
                            print("\n=== TAMBAH HERO ===")
                            
                            role_list = list(hero_meta.keys())
                            pilih_role = input(f"Pilih role (1-{len(role_list)}): ")
                            
                            if pilih_role.isdigit():
                                index_role = int(pilih_role) - 1
                                
                                if index_role >= 0 and index_role < len(role_list):
                                    role_dipilih = role_list[index_role]
                                    nama_hero = input(f"Nama hero baru: ")
                                    
                                    if nama_hero == "":
                                        print("Nama tidak boleh kosong!")
                                    else:
                                        ada, role_lama = cari_hero(nama_hero)
                                        if ada:
                                            print(f"Hero sudah ada di {role_lama}!")
                                        else:
                                            hero_meta[role_dipilih].append(nama_hero)
                                            print(f"Hero '{nama_hero}' ditambahkan!")
                                else:
                                    print("Pilihan salah!")
                            else:
                                print("Harus angka!")
                            input("\nTekan enter unutk melanjutkan...")
                            
                        elif pilih_admin == "3":
                            tampilkan_hero()
                            print("\n=== HAPUS HERO ===")
                            
                            role_list = list(hero_meta.keys())
                            pilih_role = input(f"Pilih role (1-{len(role_list)}): ")
                            
                            if pilih_role.isdigit():
                                index_role = int(pilih_role) - 1
                                
                                if index_role >= 0 and index_role < len(role_list):
                                    role_dipilih = role_list[index_role]
                                    
                                    if len(hero_meta[role_dipilih]) == 0:
                                        print("Tidak ada hero!")
                                    else:
                                        print(f"\nHero di {role_dipilih}:")
                                        no = 1
                                        for hero in hero_meta[role_dipilih]:
                                            print(f"{no}. {hero}")
                                            no = no + 1
                                        
                                        pilih_hero = input(f"\nPilih hero (1-{len(hero_meta[role_dipilih])}): ")
                                        
                                        if pilih_hero.isdigit():
                                            index_hero = int(pilih_hero) - 1
                                            
                                            if index_hero >= 0 and index_hero < len(hero_meta[role_dipilih]):
                                                hero_hapus = hero_meta[role_dipilih][index_hero]
                                                hero_meta[role_dipilih].pop(index_hero)
                                                print(f"Hero '{hero_hapus}' dihapus!")
                                            else:
                                                print("Pilihan salah!")
                                        else:
                                            print("Harus angka!")
                                else:
                                    print("Pilihan salah!")
                            else:
                                print("Harus angka!")
                            input("\nTekan enter untuk melanjutkan")
                            
                        elif pilih_admin == "4":
                            nama_cari = input("\nNama hero: ")
                            ketemu, role = cari_hero(nama_cari)
                            if ketemu:
                                print(f"Hero '{nama_cari}' ada di role {role}")
                            else:
                                print(f"Hero '{nama_cari}' tidak ada")
                            input("\nTekan enter unutk melanjutkan")
                            
                        elif pilih_admin == "5":
                            tampilkan_statistik()
                            input("\nTekan enter unutk melanjutkan")
                            
                        elif pilih_admin == "6":
                            print("\nLogout berhasil!")
                            menu_admin = False
                        else:
                            print("Pilihan salah!")
                    except:
                        print("Terjadi error!")
            else:
                print("\nLogin gagal!")
                
        elif pilih == "4":
            print("\n" + "="*50)
            print("Terima kasih!")
            print("="*50)
            lanjut = False
        else:
            print("Pilihan salah!")
    except:
        print("\nTerjadi error!")