from data import hero_meta, pengguna_baru

def cek_login(usser, pw, tipe):
    if tipe == "user":
        return usser in pengguna_baru and pengguna_baru[usser] == pw
    elif tipe == "admin":
        return usser == "admin" and pw == "admin123"
    return False

def daftar_user():
    print("\n=== DAFTAR USER BARU ===")
    user_baru = input("Username: ")
    
    if user_baru == "":
        print("Username tidak boleh kosong!")
        return
    
    if user_baru in pengguna_baru:
        print("Username sudah ada!")
        return
    
    pw_baru = input("Password: ")
    
    if len(pw_baru) < 6:
        print("Password minimal 6 karakter!")
        return
    
    pengguna_baru[user_baru] = pw_baru
    print("Berhasil daftar!")

def tampilkan_hero():
    print("\n" + "="*50)
    print("DAFTAR HERO META")
    print("="*50)
    
    nomor = 1
    for role in hero_meta:
        print(f"\n{nomor}. {role}:")
        i = 1
        for hero in hero_meta[role]:
            print(f"   {i}. {hero}")
            i += 1
        nomor += 1
    print("="*50)

def cari_hero(nama):
    for role in hero_meta:
        if nama in hero_meta[role]:
            return True, role
    return False, None

def tampilkan_statistik():
    print("\n" + "="*50)
    print("STATISTIK HERO")
    print("="*50)
    
    total = 0
    for role in hero_meta:
        jumlah = len(hero_meta[role])
        print(f"{role}: {jumlah} hero")
        total += jumlah
    
    print(f"\nTotal Hero: {total}")
    print(f"Total Role: {len(hero_meta)}")
    print("="*50)

def tambah_hero():
    tampilkan_hero()
    print("\n=== TAMBAH HERO ===")
    
    role_list = list(hero_meta.keys())
    i = 1
    for role in role_list:
        print(f"{i}. {role}")
        i += 1
    
    pilih = input(f"\nPilih role (1-{len(role_list)}): ")
    
    if not pilih.isdigit():
        print("Harus angka!")
        return
    
    index = int(pilih) - 1
    if index < 0 or index >= len(role_list):
        print("Pilihan salah!")
        return
    
    role_dipilih = role_list[index]
    nama = input("Nama hero: ")
    
    if nama == "":
        print("Nama tidak boleh kosong!")
        return
    
    ada, role_lama = cari_hero(nama)
    if ada:
        print(f"Hero sudah ada di {role_lama}!")
        return
    
    hero_meta[role_dipilih].append(nama)
    print(f"Hero '{nama}' berhasil ditambahkan!")

def hapus_hero():
    tampilkan_hero()
    print("\n=== HAPUS HERO ===")
    
    role_list = list(hero_meta.keys())
    i = 1
    for role in role_list:
        print(f"{i}. {role}")
        i += 1
    
    pilih = input(f"\nPilih role (1-{len(role_list)}): ")
    
    if not pilih.isdigit():
        print("Harus angka!")
        return
    
    index = int(pilih) - 1
    if index < 0 or index >= len(role_list):
        print("Pilihan salah!")
        return
    
    role_dipilih = role_list[index]
    
    if len(hero_meta[role_dipilih]) == 0:
        print("Tidak ada hero!")
        return
    
    print(f"\nHero di {role_dipilih}:")
    i = 1
    for hero in hero_meta[role_dipilih]:
        print(f"{i}. {hero}")
        i += 1
    
    pilih_hero = input(f"\nPilih hero (1-{len(hero_meta[role_dipilih])}): ")
    
    if not pilih_hero.isdigit():
        print("Harus angka!")
        return
    
    index_hero = int(pilih_hero) - 1
    if index_hero < 0 or index_hero >= len(hero_meta[role_dipilih]):
        print("Pilihan salah!")
        return
    
    hero_hapus = hero_meta[role_dipilih].pop(index_hero)
    print(f"Hero '{hero_hapus}' berhasil dihapus!")