import pandas as pd
import os
import subprocess
import time
# Function ntuk membersihkan terminal
def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')
# Function untuk menampilkan waktu dan tanggal saat ini dalam bentuk dictionary
def Jam():
    waktu = time.localtime()
    waktu_dict = {'jam':time.strftime("%H:%M:%S",waktu) ,'tanggal':waktu.tm_mday, 'bulan':waktu.tm_mon, 'tahun':waktu.tm_year}
    return waktu_dict
# Function untuk login dan mengecek role user yang login apakah admin atau pegawai
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
# Function untuk menampilkan menu sesuai role user yang login
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
        print("║│  3. Update Data Produk         │║")
        print("║│  4. Terima Dispatch            │║")
        print("║│  5. Absensi                    │║")
        print("║│  6. Keluar                     │║")
        print("║├────────────────────────────────┤║")
        print(f"║│ Pegawai : {user}{' '*(21-len(user))}│║")
        print("║└────────────────────────────────┘║")
    else:
        print("║│                                │║")
        print("║│  1. Daftar Produk              │║")
        print("║│  2. Cari Produk                │║")
        print("║│  3. Update Data Produk         │║")
        print("║│  4. Hapus Produk               │║")
        print("║│  5. Absensi pegawai            │║")
        print("║│  6. Histori Dispatch           │║")
        print("║│  7. Dispatch                   │║")
        print("║│  8. Mitra                      │║")
        print("║│  9. Keluar                     │║")
        print("║├────────────────────────────────┤║")
        print("║│            Menu Admin          │║")
        print("║└────────────────────────────────┘║")
    print("╚══════════════════════════════════╝")
# Function untuk mencari produk berdasarkan nama
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
    data = data[data["view"]==1]
    data = data.drop(columns=["view"])
    cari = input("Masukkan nama produk yang ingin dicari: ")
    hasil = data[data['nama'].str.contains(cari, case=False, na=False)]
    
    if hasil.empty == False :
        print(hasil.to_string(index=False))
    else:
        print("\n<==> Produk tidak ditemukan <==>")

    input("\nTekan enter untuk kembali ke menu")
    Clear_terminal()
    
# Function untuk menampilkan daftar produk yang tersedia 
def Daftar_produk():
    list =pd.read_csv("produk.csv")
    list = list[list["view"]==1]
    list = list.drop(columns=["view"])
    list_teks ="""
 _      _     _     _____               _       _    
| |    (_)   | |   |  __ \             | |     | |   
| |     _ ___| |_  | |__) | __ ___   __| |_   _| | __
| |    | / __| __| |  ___/ '__/ _ \ / _` | | | | |/ /
| |____| \__ \ |_  | |   | | | (_) | (_| | |_| |   < 
|______|_|___/\__| |_|   |_|  \___/ \__,_|\__,_|_|\_\
    
"""
    print(list_teks)
    print(list.to_string(index=False))
    
    input("\nTekan enter untuk kembali ke menu")
    Clear_terminal()
# Function untuk menambahkan data absensi pegawai ke file csv absensi.csv
def Input_absen(username):
    waktu = time.localtime()
    absensi = pd.read_csv("absensi.csv")
    absenow = absensi[(absensi['username'] == username) & 
                     (absensi['tanggal'] == waktu.tm_mday) & 
                     (absensi['bulan'] == waktu.tm_mon) & 
                     (absensi['tahun'] == waktu.tm_year)]
    notabsen = absenow.empty
    waktu_dict = {
        "username":username,
        'jam':time.strftime("%H:%M:%S",waktu) ,
        'tanggal':waktu.tm_mday,
        'bulan':waktu.tm_mon,
        'tahun':waktu.tm_year}
    df = pd.DataFrame(waktu_dict,index=[0])
    if notabsen:
        df.to_csv("absensi.csv",mode='a',header=False ,index=False)
    else:
        print(f"Anda sudah absen pada {absenow['jam'].to_string(index=False)}")
# Fuction untuk menambahkan data produk ke file csv produk.csv dan mengupdate data produk yang sudah ada
def Update_produk():
    pdProduk = pd.read_csv("produk.csv")
    pdview = pdProduk[pdProduk["view"]==1]  
    pdview = pdview.drop(columns=["view"],)
    list_teks ="""
  _    _           _       _       _____               _       _    
 | |  | |         | |     | |     |  __ \             | |     | |   
 | |  | |_ __   __| | __ _| |_ ___| |__) | __ ___   __| |_   _| | __
 | |  | | '_ \ / _` |/ _` | __/ _ \  ___/ '__/ _ \ / _` | | | | |/ /
 | |__| | |_) | (_| | (_| | ||  __/ |   | | | (_) | (_| | |_| |   < 
  \____/| .__/ \__,_|\__,_|\__\___|_|   |_|  \___/ \__,_|\__,_|_|\_\
        | |                                                         
        |_|                                                                                                                                                                               
"""
    print(list_teks)
    print(pdview.to_string(index=False))
    print("")
    print(" [1] Tambah Produk")
    print(" [2] Edit Produk\n")    
    pilih = input("Pilih Menu : ")
    Clear_terminal()
    match pilih:
        case "1":
            namapd = list(pdProduk["nama"])
            nama = input("Masukkan nama produk : ")
            if nama in namapd or nama == "":
                if nama in namapd:
                    print("Nama produk sudah ada !!")
                elif nama =="":
                    print("Nama produk tidak boleh kosong !! ")
                keluar = input("Tekan enter untuk melanjutkan / n untuk keluar ke menu")
                if keluar == "n":
                    Clear_terminal()
                    return
                else:
                    Update_produk()
                    
            harga = input("Masukkan harga produk : ")
            stok = input("Masukkan stok produk : ")
            if pdProduk.shape[0] == 0:
                newProduk = pd.DataFrame({
                    "id":[1],
                    "nama":[nama],
                    "harga":[harga],
                    "stok":[stok],
                    "view":[1],
                })
                newProduk.to_csv("produk.csv",mode ="a",index=False,header=False)
                print("Produk berhasil ditambahkan")
            else:   
                newProduk = pd.DataFrame({
                "id":[pdProduk.iloc[-1]["id"]+1],
                "nama":[nama],
                "harga":[harga],
                "stok":[stok],
                "view":[1],
                })
                newProduk.to_csv("produk.csv",mode ="a",index=False,header=False)
                print("Produk berhasil ditambahkan")
            input("Tekan enter untuk kembali ke menu")  
            Clear_terminal()
        case "2":
            print(pdProduk.to_string(index=False))
            try:
                edit = int(input("Masukkan id produk yang akan diedit : "))
                nama = input("Masukkan nama produk : ")
                harga = int(input("Masukkan harga produk : "))
                stok = int(input("Masukkan stok produk : "))
                pdProduk.loc[pdProduk['id'] == int(edit),['nama','harga',"stok"]] = [nama,harga,stok]
                pdProduk.to_csv("produk.csv",index=False)
                print("Produk berhasil diedit")
            except:
                print("Input tidak valid")
                lanjut = input("Tekan enter untuk Lanjut / ketik n untuk kembali ke menu : ")
                if lanjut != "n":
                    Update_produk()
                else:
                    return
        case _:
            return

# Function untuk menghapus data produk dari file csv produk.csv  
def Hapus_produk():
    hapusteks ="""

  _    _                         _____               _       _    
 | |  | |                       |  __ \             | |     | |   
 | |__| | __ _ _ __  _   _ ___  | |__) | __ ___   __| |_   _| | __
 |  __  |/ _` | '_ \| | | / __| |  ___/ '__/ _ \ / _` | | | | |/ /
 | |  | | (_| | |_) | |_| \__ \ | |   | | | (_) | (_| | |_| |   < 
 |_|  |_|\__,_| .__/ \__,_|___/ |_|   |_|  \___/ \__,_|\__,_|_|\_\
              | |                                                 
              |_|"""
    print(hapusteks)
    pdProduk = pd.read_csv("produk.csv")    
    pdProduk = pdProduk[pdProduk["view"]==1]
    pdview = pdProduk.drop(columns=["view"])
    print(pdview.to_string(index=False))
    print("")
    hapus = input("Pilih produk yang akan dihapus (id)")
    if hapus.isdigit() == False:
        print("Input tidak valid")
        input("Tekan enter untuk kembali ke menu")
        Clear_terminal()
        return
    pdProduk.loc[pdProduk["id"]==int(hapus),["view"]] = 0
    pdProduk.to_csv("produk.csv",index=False)
    print("Produk berhasil dihapus")
    input("Tekan enter untuk kembali ke menu")
    Clear_terminal()
    
def Cari_absen(collum,data):
    df = pd.read_csv("absensi.csv")
    if collum == "bulan" or collum == "tahun" or collum == "tanggal":
        df = df[df[collum] == int(data)]
    else:
        df = df[df[collum].str.contains(data,case=False)]
    if df.empty:
        print("\n  Data Kosong")
        return
    print(df.to_string(index=False))
    if collum=="bulan":
        keterangan = "bulan "
    if collum=="tahun":
        keterangan = "tahun "
    if collum=="tanggal":
        keterangan = "tanggal "
    else:
        keterangan = ""
    print(f"Jumlah Data {keterangan}{data} :",df.shape[0])
    
# Function untuk menampilkan data absensi pegawai berdasarkan bulan, tahun, tanggal, dan username
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

# Function untuk menampilkan data mitra dan menambahkan, menghapus, dan mengedit data mitra
def Mitra(): 
    teksmitra = """

  __  __ _ _               _______          _ _______         _ 
 |  \/  (_) |             |__   __|        (_)__   __|       (_)
 | \  / |_| |_ _ __ __ _     | | __ _ _ __  _   | | ___  _ __ _ 
 | |\/| | | __| '__/ _` |    | |/ _` | '_ \| |  | |/ _ \| '__| |
 | |  | | | |_| | | (_| |    | | (_| | | | | |  | | (_) | |  | |
 |_|  |_|_|\__|_|  \__,_|    |_|\__,_|_| |_|_|  |_|\___/|_|  |_|
 """
    print(teksmitra)
    mitra = pd.read_csv("mitra.csv")
    print(mitra.to_string(index=False) + "\n")
    print("1. Tambah Mitra")
    print("2. Hapus Mitra")
    print("3. Edit Mitra")
    menu = input("Pilih Menu : ")
    match menu:
        case "1":
            nama = input("Masukkan nama mitra : ")
            alamat = input("Masukkan alamat mitra : ")
            if mitra.shape[0] == 0:
                newMitra = pd.DataFrame({
                    "id":[1],
                    "nama":[nama],
                    "alamat":[alamat],
                })
                newMitra.to_csv("mitra.csv",mode ="a",index=False,header=False)
                print("Mitra berhasil ditambahkan")
            else:   
                newMitra = pd.DataFrame({
                "id":[mitra.iloc[-1]["id"]+1],
                "nama":[nama],
                "alamat":[alamat],
                })
                newMitra.to_csv("mitra.csv",mode ="a",index=False,header=False)
                print("Mitra berhasil ditambahkan")
        case "2":
            id = input("Masukkan id mitra : ")
            mitra = mitra[mitra['id'] != int(id)]
            mitra.to_csv("mitra.csv",index=False)
            print("Mitra berhasil dihapus")
            
        case "3":
            edit = input("Masukkan id mitra yang akan diedit : ")
            nama = input("Masukkan nama mitra : ")
            alamat = input("Masukkan alamat mitra : ")
            mitra.loc[mitra["id"]==int(edit),["nama","alamat"]]= [nama,alamat]
            print(mitra.to_string(index=False))
            mitra.to_csv("mitra.csv",index=False)
            print("Mitra berhasil diedit")
        case _:
            Clear_terminal()
            return
    input("Tekan enter untuk kembali ke menu")
    Clear_terminal()
            
# Function untuk menampilkan data dispatch dan menambahkan data dispatch yang baru 
def Dispatch(user):
    dfPegawai = pd.read_csv("users.csv")
    userole = dfPegawai[dfPegawai['username'] == user]['role'].values[0]
    username = dfPegawai[dfPegawai['username'] == user]['username'].values[0]
    idPegawai= dfPegawai[dfPegawai['username'] == user]['id'].values[0]
    dfProduk = pd.read_csv("produk.csv")
    dfDispatch = pd.read_csv("dispatch.csv")
    dfMitra = pd.read_csv("mitra.csv")
    if userole == "pegawai":
        pegawaiDispatch = """
  ____  _                 _       _     
 |  _ \(_)___ _ __   __ _| |_ ___| |__  
 | | | | / __| '_ \ / _` | __/ __| '_ \ 
 | |_| | \__ \ |_) | (_| | || (__| | | |
 |____/|_|___/ .__/ \__,_|\__\___|_| |_|
             |_|                       
"""
        print(pegawaiDispatch)
        dfDispatch = pd.read_csv("dispatch.csv")
        dfDispatch = dfDispatch[dfDispatch['status'] == "proses"]
        dfDispatch = dfDispatch[dfDispatch['id_pegawai'] == idPegawai]
        dfDisplay = pd.DataFrame()
        dfDisplay['id'] = dfDispatch['id']
        dfDisplay['mitra'] = dfDispatch['id_mitra'].map(dfMitra.set_index('id')['nama'])
        dfDisplay['alamat'] = dfDispatch['id_mitra'].map(dfMitra.set_index('id')['alamat'])
        dfDisplay['produk'] = dfDispatch['id_barang'].map(dfProduk.set_index('id')['nama'])
        dfDisplay['jumlah'] = dfDispatch['jumlah']
        dfDisplay['tanggal'] = dfDispatch['tanggal']
        dfDisplay['jam'] = dfDispatch['jam']
        dfDisplay['status'] = dfDispatch['status']
        if dfDisplay.shape[0] == 0:
            print("Tidak ada dispatch yang perlu diselesaikan")
            input("Tekan enter untuk kembali ke menu")
            Clear_terminal()
            return
        else:
            print(dfDisplay.to_string(index=False))
            id_dispatch = input("\nMasukkan id dispatch yang sudah selesai : ")
            input("Tekan enter untuk kembali ke menu")
            dfDispatch.loc[dfDispatch['id'] == int(id_dispatch),'status'] = "selesai"
            dfDispatch.to_csv("dispatch.csv",index=False)
            Clear_terminal()
            return

    if userole == "admin":
        adminDispatch = """
              _           _         _____  _                 _       _     
     /\      | |         (_)       |  __ \(_)               | |     | |    
    /  \   __| |_ __ ___  _ _ __   | |  | |_ ___ _ __   __ _| |_ ___| |__  
   / /\ \ / _` | '_ ` _ \| | '_ \  | |  | | / __| '_ \ / _` | __/ __| '_ \ 
  / ____ \ (_| | | | | | | | | | | | |__| | \__ \ |_) | (_| | || (__| | | |
 /_/    \_\__,_|_| |_| |_|_|_| |_| |_____/|_|___/ .__/ \__,_|\__\___|_| |_|
                                                | |                        
                                                |_|"""
        print(adminDispatch)
        dfProdukDisplay = dfProduk[dfProduk['view'] == 1]
        dfProdukDisplay = dfProduk.drop(columns=["view"])
        print(dfProdukDisplay.to_string(index=False))
        try:
            id_produk = input("\nMasukkan id produk yang akan didispatch : ")
            if id_produk.isdigit() == False:
                Clear_terminal()
                return
            jumlah = input("Masukkan jumlah produk yang akan didispatch : ")
            if dfProduk[dfProduk['id'] == int(id_produk)]['stok'].values[0] < int(jumlah):
                print("Stok tidak mencukupi")
                input("Tekan enter untuk kembali ke menu")
                return
            else:
                dfProduk.loc[dfProduk['id'] == int(id_produk),'stok'] = dfProduk[dfProduk['id'] == int(id_produk)]['stok'] - int(jumlah)

            print(dfMitra.to_string(index=False))
            mitra = input("Pilih mitra yang akan menerima dispatch (id) : ")
            print(dfPegawai[dfPegawai['role'] == "pegawai"][['id','username','role']].to_string(index=False))
            id_pegawai = input("Pilih pegawai yang akan melakukan dispatch (id) : ")
        except:
            Clear_terminal()
            print("Input tidak valid")
            lanjut = input("Tekan enter untuk Lanjut / ketik n untuk kembali ke menu : ")
            if lanjut != "n":
                Dispatch(user)
            else:
                return
        if dfDispatch.shape[0] == 0:
            DispatchDict = pd.Series({
                "id":1,
                "id_pegawai":id_pegawai,
                "id_mitra":mitra,    
                "id_barang":id_produk,
                "jumlah":jumlah,
                "tanggal":time.strftime("%d/%m/%Y"),
                "jam":time.strftime("%H:%M:%S"),
                "status":"proses"
            })
            dispatch = pd.DataFrame(DispatchDict).T
            dispatch.to_csv("dispatch.csv",index=False)
        else:
            DispatchDict = pd.Series({
                "id":dfDispatch.iloc[-1]["id"]+1,
                "id_pegawai":id_pegawai,
                "id_mitra":mitra,    
                "id_barang":id_produk,
                "jumlah":jumlah,
                "tanggal":time.strftime("%d/%m/%Y"),
                "jam":time.strftime("%H:%M:%S"),
                "status":"proses"
            })
        print(DispatchDict)
        dispatch = dfDispatch._append(DispatchDict,ignore_index=True)
        dispatch.to_csv("dispatch.csv",index=False)
        dfProduk.to_csv("produk.csv",index=False)
        input("Tekan enter untuk kembali ke menu")
        Clear_terminal()

# Function untuk menampilkan data dispatch yang sudah selesai 
def View_Dispatch():
    ViewTeks = """

  _    _ _     _             _   _____  _                 _       _     
 | |  | (_)   | |           (_) |  __ \(_)               | |     | |    
 | |__| |_ ___| |_ ___  _ __ _  | |  | |_ ___ _ __   __ _| |_ ___| |__  
 |  __  | / __| __/ _ \| '__| | | |  | | / __| '_ \ / _` | __/ __| '_ \ 
 | |  | | \__ \ || (_) | |  | | | |__| | \__ \ |_) | (_| | || (__| | | |
 |_|  |_|_|___/\__\___/|_|  |_| |_____/|_|___/ .__/ \__,_|\__\___|_| |_|
                                             | |                        
                                             |_|"""
    dfDispatch = pd.read_csv("dispatch.csv")
    dfProduk = pd.read_csv("produk.csv")
    dfMitra = pd.read_csv("mitra.csv")
    dfPegawai = pd.read_csv("users.csv")
    dfDisplay = pd.DataFrame()
    dfDisplay['id'] = dfDispatch['id']
    dfDisplay['mitra'] = dfDispatch['id_mitra'].map(dfMitra.set_index('id')['nama'])
    dfDisplay['alamat'] = dfDispatch['id_mitra'].map(dfMitra.set_index('id')['alamat'])
    dfDisplay['produk'] = dfDispatch['id_barang'].map(dfProduk.set_index('id')['nama'])
    dfDisplay['jumlah'] = dfDispatch['jumlah']
    dfDisplay['tanggal'] = dfDispatch['tanggal']
    dfDisplay['jam'] = dfDispatch['jam']
    dfDisplay['status'] = dfDispatch['status']
    dfDisplay['pegawai'] = dfDispatch['id_pegawai'].map(dfPegawai.set_index('id')['username'])
    print(ViewTeks)
    print("Menu Histori Dispatch")
    print("1. Tampilkan Dispatch Hari Ini")
    print("2. Tampilkan Dispatch Bulan Ini")
    print("3. Tampilkan Semua Dispatch")
    print("4. Cari Dispatch Pegawai\n")
    pilih = input("Pilih Menu : ")
    Clear_terminal()
    match pilih:
        case "1":
            dfDisplay = dfDisplay[dfDisplay['tanggal'] == time.strftime("%d/%m/%Y")]
            print(dfDisplay.to_string(index=False))
            input("\nTekan enter untuk kembali ke menu")
            Clear_terminal()
        case "2":
            dfDisplay = dfDisplay[dfDisplay['tanggal'].str.contains(time.strftime("%m/%Y"))]
            print(dfDisplay.to_string(index=False))
            input("\nTekan enter untuk kembali ke menu"   )
            Clear_terminal()
        case "3":
            print(dfDisplay.to_string(index=False))
            input("\nTekan enter untuk kembali ke menu")
            Clear_terminal()
        case "4":
            dfDisplay = dfDisplay[dfDisplay['pegawai'].str.contains(input("Masukkan username pegawai : "),case=False)]
            print(dfDisplay.to_string(index=False))
            input("\nTekan enter untuk kembali ke menu")
            Clear_terminal()
        case _:
            Clear_terminal()
    
# ======================================================================================================================    
# Menu utama program
# Variable username dan role untuk menyimpan data username dan role user yang login
username,role = login()

# Looping menu utama program 
while True:
    # Menampilkan menu sesuai role user yang login
    Menu(username,role)
    # Menampilkan menu sesuai role user yang login
    # Menu untuk pegawai
    if role == "pegawai":
        menu = input("  Pilih menu: ")
        match menu:
            case "1":
                Clear_terminal()
                Daftar_produk()
            case "2":
                Clear_terminal()
                Cari_produk()
            case "3":
                Clear_terminal()
                Update_produk()
            case "4":
                Clear_terminal()
                Dispatch(username)
            case "5":
                Clear_terminal()
                Absensi(username)
            case "6":
                Clear_terminal()
                break
            case _:
                Clear_terminal()
    # Menu untuk admin   
    elif role == "admin":
        menu = input("  Pilih menu: ")
        match menu:
            case "1":
                Clear_terminal()
                Daftar_produk()
            case "2":
                Clear_terminal()
                Cari_produk()
            case "3":
                Clear_terminal()
                Update_produk()
            case "4":
                Clear_terminal()
                Hapus_produk()
            case "5":
                Clear_terminal()
                Absensi(username)
            case "6":
                Clear_terminal()
                View_Dispatch()
            case "7":
                Clear_terminal()
                Dispatch(username)
            case "8":
                Clear_terminal()
                Mitra()
            case "9":
                break
            case _:
                Clear_terminal()
                



