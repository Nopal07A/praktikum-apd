import os
from fungsi import *

def main():
    os.system('clear')
    
    while True:
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
            input("\nTekan enter...")
        
        elif pilih == "2":
            print("\n=== LOGIN USER ===")
            user = input("Username: ")
            pw = input("Password: ")
            
            if cek_login(user, pw, "user"):
                print("\nLogin berhasil!")
                input("Tekan enter...")
                
                while True:
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
                        input("\nTekan enter...")
                    
                    elif pilih_user == "2":
                        nama = input("\nNama hero: ")
                        ketemu, role = cari_hero(nama)
                        if ketemu:
                            print(f"Hero '{nama}' ada di role {role}")
                        else:
                            print("Hero tidak ditemukan!")
                        input("\nTekan enter...")
                    
                    elif pilih_user == "3":
                        tampilkan_statistik()
                        input("\nTekan enter...")
                    
                    elif pilih_user == "4":
                        print("\nLogout berhasil!")
                        break
                    
                    else:
                        print("Pilihan salah!")
            else:
                print("\nLogin gagal!")
                input("\nTekan enter...")
        
        elif pilih == "3":
            print("\n=== LOGIN ADMIN ===")
            user = input("Username: ")
            pw = input("Password: ")
            
            if cek_login(user, pw, "admin"):
                print("\nSelamat datang, Admin!")
                input("Tekan enter...")
                
                while True:
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
                        input("\nTekan enter...")
                    
                    elif pilih_admin == "2":
                        tambah_hero()
                        input("\nTekan enter...")
                    
                    elif pilih_admin == "3":
                        hapus_hero()
                        input("\nTekan enter...")
                    
                    elif pilih_admin == "4":
                        nama = input("\nNama hero: ")
                        ketemu, role = cari_hero(nama)
                        if ketemu:
                            print(f"Hero '{nama}' ada di role {role}")
                        else:
                            print("Hero tidak ditemukan!")
                        input("\nTekan enter...")
                    
                    elif pilih_admin == "5":
                        tampilkan_statistik()
                        input("\nTekan enter...")
                    
                    elif pilih_admin == "6":
                        print("\nLogout berhasil!")
                        break
                    
                    else:
                        print("Pilihan salah!")
            else:
                print("\nLogin gagal!")
                input("\nTekan enter...")
        
        elif pilih == "4":
            print("\n" + "="*50)
            print("Terima kasih!")
            print("="*50)
            break
        
        else:
            print("Pilihan salah!")
main()

