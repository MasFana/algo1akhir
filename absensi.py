from ast import In
import pandas as pd
from tabulate import tabulate
import time
import os
import subprocess

def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None) 

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
    
def Jam():
    waktu = time.localtime()
    waktu_dict = {'jam':time.strftime("%H:%M:%S",waktu) ,'tanggal':waktu.tm_mday, 'bulan':waktu.tm_mon, 'tahun':waktu.tm_year}
    return waktu_dict

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
                
                input("\nTekan enter untuk kembali ke menu")
                Clear_terminal()
            case "3":
                print(" Cari Absensi Pegawai") 
                
                input("\nTekan enter untuk kembali ke menu")
                Clear_terminal()
    elif role == 'pegawai':
        print(berhasil_teks) 
        print("> USER :",username)
        Input_absen(username)
        input("\nTekan enter untuk kembali ke menu")
        Clear_terminal()
Absensi('fana')