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
user = "admin"
pw = "admin123"

bool = True
while bool:
    print("\n" + "="*50)
    print("SISTEM MANAGEMENT HERO META".center(50))
    print("="*50)
    print("1. Daftar pengguna baru")
    print("2. Login sebagai user")
    print("3. Login sebagai admin")
    print("4. Keluar")
    print("="*50)
    pilih = input("\nPilihan login (1-4): ")
    
    if pilih == "1":
        print("\n=== DAFTAR PENGGUNA BARU ===")
        print("LOGIN SEBAGAI PENGGUNA BARU")
        usnbaru = input("\nMasukkan Username baru : ")
        pwbaru = input("\nMasukkan Password baru : ")
        pengguna_baru[usnbaru] = pwbaru
        print(f"\nUser dengan username {usnbaru} telah terdaftar")
        
    elif pilih == "2":
        print("\n=== LOGIN SEBAGAI USER ===")
        usn_input = input("\nMasukkan username anda : ")
        pw_input = input("\nMasukkan password anda : ")
        
        if usn_input in pengguna_baru and pengguna_baru[usn_input] == pw_input:
            print("\nANDA BERHASIL LOGIN")
            input("\nTekan enter untuk lanjutkan program")
            
            bool_user = True
            while bool_user:
                print("\n" + "="*50)
                print("MENU USER".center(50))
                print("="*50)
                print("1. Lihat daftar hero")
                print("2. Logout")
                print("="*50)
                pilihan = input("\nPilih menu (1-2): ")
                
                if pilihan == "1":
                    print("\n" + "="*50)
                    print("DAFTAR HERO META".center(50))
                    print("="*50)
                    roles_list = list(hero_meta.keys())
                    for i in range(len(roles_list)):
                        print(f"\n{i+1}. {roles_list[i]}:")
                        heroes = hero_meta[roles_list[i]]
                        for j in range(len(heroes)):
                            print(f"   {j+1}. {heroes[j]}")
                    print("="*50)
                    input("\nTekan enter untuk kembali")
                    
                elif pilihan == "2":
                    print("\nLogout berhasil!")
                    bool_user = False
                else:
                    print("\nPilihan tidak valid!")
        else:
            print("\nANDA BELUM TERDAFTAR")
            
    elif pilih == "3":
        print("\n=== LOGIN SEBAGAI ADMIN ===")
        usn_input = input("Masukkan username anda: ")
        pw_input = input("Masukkan password anda: ")
        
        if usn_input == user and pw_input == pw:
            print(f"\nSelamat datang, Admin {usn_input}!")
            
            bool_admin = True
            while bool_admin:
                print("\n" + "="*50)
                print("MENU ADMIN".center(50))
                print("="*50)
                print("1. Lihat daftar hero")
                print("2. Tambah hero")
                print("3. Hapus hero")
                print("4. Logout")
                print("="*50)
                pilihan = input("\nPilih menu (1-4): ")
                
                if pilihan == "1":
                    print("\n" + "="*50)
                    print("DAFTAR HERO META".center(50))
                    print("="*50)
                    roles_list = list(hero_meta.keys())
                    for i in range(len(roles_list)):
                        print(f"\n{i+1}. {roles_list[i]}:")
                        heroes = hero_meta[roles_list[i]]
                        for j in range(len(heroes)):
                            print(f"   {j+1}. {heroes[j]}")
                    print("="*50)
                    input("\nTekan enter untuk kembali")
                    
                elif pilihan == "2":
                    print("\n" + "="*50)
                    print("DAFTAR HERO META".center(50))
                    print("="*50)
                    roles_list = list(hero_meta.keys())
                    for i in range(len(roles_list)):
                        print(f"\n{i+1}. {roles_list[i]}:")
                        heroes = hero_meta[roles_list[i]]
                        for j in range(len(heroes)):
                            print(f"   {j+1}. {heroes[j]}")
                    print("="*50)
                    
                    print("\n=== TAMBAH HERO BARU ===")
                    role_pilih = input(f"\nPilih role (1-{len(hero_meta)}): ")
                    
                    if role_pilih.isdigit():
                        role_idx = int(role_pilih) - 1
                        if 0 <= role_idx < len(roles_list):
                            role_terpilih = roles_list[role_idx]
                            nama_hero = input(f"Masukkan nama hero baru untuk {role_terpilih}: ")
                            
                            if nama_hero != "":
                                hero_ada = False
                                for role in hero_meta:
                                    if nama_hero in hero_meta[role]:
                                        hero_ada = True
                                        break
                                
                                if hero_ada:
                                    print(f"\nHero '{nama_hero}' sudah ada dalam list!")
                                else:
                                    hero_meta[role_terpilih].append(nama_hero)
                                    print(f"\nHero '{nama_hero}' berhasil ditambahkan ke role {role_terpilih}!")
                            else:
                                print("\nNama hero tidak boleh kosong!")
                        else:
                            print("\nPilihan role tidak valid!")
                    else:
                        print("\nInput harus berupa angka 1-5!")
                    input("\nTekan enter untuk kembali")
                    
                elif pilihan == "3":
                    print("\n" + "="*50)
                    print("DAFTAR HERO META".center(50))
                    print("="*50)
                    roles_list = list(hero_meta.keys())
                    for i in range(len(roles_list)):
                        print(f"\n{i+1}. {roles_list[i]}:")
                        heroes = hero_meta[roles_list[i]]
                        for j in range(len(heroes)):
                            print(f"   {j+1}. {heroes[j]}")
                    print("="*50)
                    
                    print("\n=== HAPUS HERO ===")
                    role_pilih = input(f"\nPilih role (1-{len(hero_meta)}): ")
                    
                    if role_pilih.isdigit():
                        role_idx = int(role_pilih) - 1
                        if 0 <= role_idx < len(roles_list):
                            role_terpilih = roles_list[role_idx]
                            
                            if len(hero_meta[role_terpilih]) == 0:
                                print(f"\nTidak ada hero di role {role_terpilih}!")
                            else:
                                print(f"\nDaftar hero di {role_terpilih}:")
                                heroes = hero_meta[role_terpilih]
                                for i in range(len(heroes)):
                                    print(f"{i+1}. {heroes[i]}")
                                
                                hero_pilih = input(f"\nPilih hero yang ingin dihapus (1-{len(hero_meta[role_terpilih])}): ")
                                
                                if hero_pilih.isdigit():
                                    hero_idx = int(hero_pilih) - 1
                                    
                                    if 0 <= hero_idx < len(hero_meta[role_terpilih]):
                                        hero_dihapus = hero_meta[role_terpilih][hero_idx]
                                        hero_meta[role_terpilih].pop(hero_idx)
                                        print(f"\nHero '{hero_dihapus}' berhasil dihapus dari role {role_terpilih}!")
                                    else:
                                        print("\nPilihan hero tidak valid!")
                                else:
                                    print("\nInput harus berupa angka!")
                        else:
                            print("\nPilihan role tidak valid!")
                    else:
                        print("\nInput harus berupa angka 1-5!")
                    input("\nTekan enter untuk kembali")
                    
                elif pilihan == "4":
                    print("\nLogout berhasil!")
                    bool_admin = False
                else:
                    print("\nPilihan tidak valid!")
        else:
            print("\nLogin gagal! Cek kembali username atau password anda")
            
    elif pilih == "4":
        print("\n" + "="*50)
        print("Terima kasih telah menggunakan program!".center(50))
        print("="*50)
        bool = False
    else:
        print("\nPilihan tidak valid! Silakan pilih 1-4")