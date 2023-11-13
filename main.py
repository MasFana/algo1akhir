import pandas as pd
import os
import subprocess
import csv
from tabulate import tabulate
import time

def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')
def Jam():
    waktu = time.localtime()
    waktu_dict = {'jam':time.strftime("%H:%M:%S",waktu) ,'tanggal':waktu.tm_mday, 'bulan':waktu.tm_mon, 'tahun':waktu.tm_year}
    return waktu_dict

def login():
    login_text = """                                            
 _                 _       
| |               (_)      
| |     ___   __ _ _ _ __  
| |    / _ \ / _` | | '_ \ 
| |___| (_) | (_| | | | | |
|______\___/ \__, |_|_| |_|
              __/ |        
             |___/                         
"""
    password_text = """
 _____                                        _ 
|  __ \                                      | |
| |__) |_ _ ___ ___ _____      _____  _ __ __| |
|  ___/ _` / __/ __/ __\ \ /\ / / _ \| '__/ _` |
| |  | (_| \__ \__ \__ \\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/___/ \_/\_/ \___/|_|  \__,_|
  _____       _       _     
 / ____|     | |     | |    
| (___   __ _| | __ _| |__  
 \___ \ / _` | |/ _` | '_ \ 
 ____) | (_| | | (_| | | | |
|_____/ \__,_|_|\__,_|_| |_|
"""
    username_text = """
 _    _               
| |  | |              
| |  | |___  ___ _ __ 
| |  | / __|/ _ \ '__|
| |__| \__ \  __/ |   
 \____/|___/\___|_|                      
 _______ _     _       _      _____  _ _                       _               
|__   __(_)   | |     | |    |  __ \(_) |                     | |              
   | |   _  __| | __ _| | __ | |  | |_| |_ ___ _ __ ___  _   _| | ____ _ _ __  
   | |  | |/ _` |/ _` | |/ / | |  | | | __/ _ \ '_ ` _ \| | | | |/ / _` | '_ \ 
   | |  | | (_| | (_| |   <  | |__| | | ||  __/ | | | | | |_| |   < (_| | | | |
   |_|  |_|\__,_|\__,_|_|\_\ |_____/|_|\__\___|_| |_| |_|\__,_|_|\_\__,_|_| |_|
"""
    while True:
        users = pd.read_csv("users.csv")
        print(login_text)
        username = input(" Username: ")
        if username in users['username'].values:
            baris_user = users[users['username'] == username]
            password = input(" Password: ")
            if password == baris_user['password'].values[0]:
                role = baris_user['role'].values[0]
                Clear_terminal()
                return username,role
            elif password != baris_user['password'].values[0]:
                Clear_terminal()
                print(password_text)
                input("Tekan Enter Untuk Melanjutkan ")
                Clear_terminal()
        else:
            Clear_terminal()
            print(username_text)
            input("Tekan Enter Untuk Melanjutkan ")
            Clear_terminal()

def Menu(user="",role="pegawai"):
    print(
"""
╔══════════════════════════════════╗
║            TaniToriPro           ║
║┌────────────────────────────────┐║""")
    if role=="pegawai":
        print("║│                                │║")
        print("║│  1. Daftar Produk              │║")
        print("║│  2. Cari Produk                │║")
        print("║│  3. Terima Dispatch            │║")
        print("║│  4. Absensi                    │║")
        print("║├────────────────────────────────┤║")
        print(f"║│ Pegawai : {user}{' '*(21-len(user))}│║")
        print("║└────────────────────────────────┘║")
    else:
        print("║│                                │║")
        print("║│  1. Daftar Produk              │║")
        print("║│  2. Cari Produk                │║")
        print("║│  3. Update Data Produk         │║")
        print("║│  4. Hapus Produk               │║")
        print("║│  5. Histori                    │║")
        print("║│  6. Absensi pegawai            │║")
        print("║│  7. Dispatch                   │║")
        print("║├────────────────────────────────┤║")
        print("║│            Menu Admin          │║")
        print("║└────────────────────────────────┘║")
    print("╚══════════════════════════════════╝")

def Cari_produk():
    cari_text = """
  _____           _   _____               _       _    
 / ____|         (_) |  __ \             | |     | |   
| |     __ _ _ __ _  | |__) | __ ___   __| |_   _| | __
| |    / _` | '__| | |  ___/ '__/ _ \ / _` | | | | |/ /
| |___| (_| | |  | | | |   | | | (_) | (_| | |_| |   < 
 \_____\__,_|_|  |_| |_|   |_|  \___/ \__,_|\__,_|_|\_\

"""
    print(cari_text)
    data =pd.read_csv("produk.csv")
    cari = input("Masukkan nama produk yang ingin dicari: ")
    hasil = data[data['nama'].str.contains(cari, case=False, na=False)]
    if hasil.empty == False :
        print(tabulate(hasil, headers='keys', tablefmt='psql'))
    else:
        print("\n<==> Produk tidak ditemukan <==>")

    input("\nTekan enter untuk kembali ke menu")
    Clear_terminal()
    
def List_produk():
    list =pd.read_csv("produk.csv")
    list_teks ="""
 _      _     _     _____               _       _    
| |    (_)   | |   |  __ \             | |     | |   
| |     _ ___| |_  | |__) | __ ___   __| |_   _| | __
| |    | / __| __| |  ___/ '__/ _ \ / _` | | | | |/ /
| |____| \__ \ |_  | |   | | | (_) | (_| | |_| |   < 
|______|_|___/\__| |_|   |_|  \___/ \__,_|\__,_|_|\_\
    
"""
    print(list_teks)
    print(tabulate(list, headers='keys', tablefmt='psql'))
    
    input("Tekan enter untuk kembali ke menu")
    Clear_terminal()

def Input_absen(username):
    waktu = time.localtime()
    waktu_dict = {
        "username":username,
        'jam':time.strftime("%H:%M:%S",waktu) ,
        'tanggal':waktu.tm_mday,
        'bulan':waktu.tm_mon,
        'tahun':waktu.tm_year}
    df = pd.DataFrame(waktu_dict,index=[0])
    df.to_csv("absensi.csv",mode='a',header=False,index=False)
 
def Cari_absen(collum,data):
    df = pd.read_csv("absensi.csv")
    if collum == "bulan" or collum == "tahun" or collum == "tanggal":
        df = df[df[collum] == int(data)]
    else:
        df = df[df[collum].str.contains(data)]
    print(tabulate(df,headers='keys',tablefmt='psql'))
    print(f"Jumlah Data {data} :",df.shape[0])
    
def Absensi(username):
    usertype = pd.read_csv("users.csv")
    role = usertype[usertype['username'] == username]['role'].values[0]
    absensi_teks ="""
          _                        _ 
    /\   | |                      (_)
   /  \  | |__  ___  ___ _ __  ___ _ 
  / /\ \ | '_ \/ __|/ _ \ '_ \/ __| |
 / ____ \| |_) \__ \  __/ | | \__ \ |
/_/    \_\_.__/|___/\___|_| |_|___/_|"""
    berhasil_teks = """ ____            _               _ _ 
|  _ \          | |             (_) |
| |_) | ___ _ __| |__   __ _ ___ _| |
|  _ < / _ \ '__| '_ \ / _` / __| | |
| |_) |  __/ |  | | | | (_| \__ \ | |
|____/ \___|_|  |_| |_|\__,_|___/_|_|
"""
    print(absensi_teks)
    
    if role == 'admin':
        print(" Absensi Hari Ini") 
        hari_ini = str(Jam()["tanggal"])
        Cari_absen("tanggal",hari_ini)
        print("""
   -- Menu absensi --          
  [1] Absensi Bulan Ini
  [2] Absensi Tahun Ini
  [3] Cari Absensi Pegawai
  
""")
        menu = input("  Pilih menu: ")
        match menu:
            case "1":
                print(" Absensi Bulan Ini") 
                Cari_absen("bulan",str(Jam()["bulan"]))
                input("\nTekan enter untuk kembali ke menu")
                Clear_terminal()
            case "2":
                print(" Absensi Tahun Ini") 
                Cari_absen("tahun",str(Jam()["tahun"]))
                input("\nTekan enter untuk kembali ke menu")
                Clear_terminal()
            case "3":
                print(" Cari Absensi Pegawai") 
                Cari_absen("username",input("Masukkan username pegawai: "))
                input("\nTekan enter untuk kembali ke menu")
                Clear_terminal()
    elif role == 'pegawai':
        print(berhasil_teks) 
        print("> USER :",username)
        Input_absen(username)
        input("\nTekan enter untuk kembali ke menu")
        Clear_terminal()


Menu(login())





