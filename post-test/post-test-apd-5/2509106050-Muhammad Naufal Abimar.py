import os
os.system('clear')

list_hero_meta = [
    ["Yve","Zhuxin","Pharsa","Zetian","Novaria","Kadita"],
    ["Floryn","Mathilda","Kalea","Angela","Badang","Grock","Gatot"],
    ["Hayabusa","Fanny","Yi_sun_shin","Lancelot","Fredrin"],
    ["Alice","Cici","Arlot","Phoveus","Gloo"],
    ["Granger","Nathan","Wanwan","Obsidia"],
]
nama_role = ["Mage","Tank/Support","Assassin","Fighter","Marksman"]
pengguna_baru = []
user = "nopal"
pw = "050"

bool_main = True
while bool_main:
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
        pengguna_baru.append([usnbaru, pwbaru])
        print(f"\nUser dengan username {usnbaru} telah terdaftar")
        
    elif pilih == "2":
        print("\n=== LOGIN SEBAGAI USER ===")
        usn_input = input("\nMasukkan username anda : ")
        pw_input = input("\nMasukkan password anda : ")
        
        login_berhasil = False
        for pengguna in pengguna_baru:
            if pengguna[0] == usn_input and pengguna[1] == pw_input:
                login_berhasil = True
                break
        
        if login_berhasil:
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
                    for i in range(len(nama_role)):
                        print(f"\n{i+1}. {nama_role[i]}:")
                        for j in range(len(list_hero_meta[i])):
                            print(f"   {j+1}. {list_hero_meta[i][j]}")
                    print("="*50)
                    input("\nTekan enter untuk kembali...")
                    
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
                    for i in range(len(nama_role)):
                        print(f"\n{i+1}. {nama_role[i]}:")
                        for j in range(len(list_hero_meta[i])):
                            print(f"   {j+1}. {list_hero_meta[i][j]}")
                    print("="*50)
                    input("\nTekan enter untuk kembali")
                    
                elif pilihan == "2":
                    
                    print("\n" + "="*50)
                    print("DAFTAR HERO META".center(50))
                    print("="*50)
                    for i in range(len(nama_role)):
                        print(f"\n{i+1}. {nama_role[i]}:")
                        for j in range(len(list_hero_meta[i])):
                            print(f"   {j+1}. {list_hero_meta[i][j]}")
                    print("="*50)
                    
                    print("\n=== TAMBAH HERO BARU ===")
                    role_pilih = input(f"\nPilih role (1-{len(nama_role)}): ")
                    
                    if role_pilih == "1" or role_pilih == "2" or role_pilih == "3" or role_pilih == "4" or role_pilih == "5":
                        role_idx = int(role_pilih) - 1
                        if role_idx >= 0 and role_idx < len(nama_role):
                            nama_hero = input(f"Masukkan nama hero baru untuk {nama_role[role_idx]}: ")
                            if nama_hero != "":
                                hero_ada = False
                                for role_list in list_hero_meta:
                                    if nama_hero in role_list:
                                        hero_ada = True
                                        break
                                if hero_ada:
                                    print(f"\nHero '{nama_hero}' sudah ada dalam list!")
                                else:
                                    list_hero_meta[role_idx].append(nama_hero)
                                    print(f"\nHero '{nama_hero}' berhasil ditambahkan ke role {nama_role[role_idx]}!")
                            else:
                                print("\nNama hero tidak boleh kosong!")
                    else:
                        print("\nInput harus berupa angka 1-5!")
                    input("\nTekan enter untuk kembali")
                    
                elif pilihan == "3":
                    
                    print("\n" + "="*50)
                    print("DAFTAR HERO META".center(50))
                    print("="*50)
                    for i in range(len(nama_role)):
                        print(f"\n{i+1}. {nama_role[i]}:")
                        for j in range(len(list_hero_meta[i])):
                            print(f"   {j+1}. {list_hero_meta[i][j]}")
                    print("="*50)
                    
                    print("\n=== HAPUS HERO ===")
                    role_pilih = input(f"\nPilih role (1-{len(nama_role)}): ")
                    
                    if role_pilih == "1" or role_pilih == "2" or role_pilih == "3" or role_pilih == "4" or role_pilih == "5":
                        role_idx = int(role_pilih) - 1
                        if role_idx >= 0 and role_idx < len(nama_role):
                            if len(list_hero_meta[role_idx]) == 0:
                                print(f"\nTidak ada hero di role {nama_role[role_idx]}!")
                            else:
                                print(f"\nDaftar hero di {nama_role[role_idx]}:")
                                for i in range(len(list_hero_meta[role_idx])):
                                    print(f"{i+1}. {list_hero_meta[role_idx][i]}")
                                hero_pilih = input(f"\nPilih hero yang ingin dihapus (1-{len(list_hero_meta[role_idx])}): ")
                                hero_idx = int(hero_pilih) - 1
                                if hero_idx >= 0 and hero_idx < len(list_hero_meta[role_idx]):
                                    hero_dihapus = list_hero_meta[role_idx][hero_idx]
                                    list_hero_meta[role_idx].pop(hero_idx)
                                    print(f"\nHero '{hero_dihapus}' berhasil dihapus dari role {nama_role[role_idx]}!")
                                else:
                                    print("\nPilihan hero tidak valid!")
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
        bool_main = False
    else:
        print("\nPilihan tidak valid! Silakan pilih 1-4")