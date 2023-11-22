
import dis
from operator import index
import pandas as pd
import time
# In Development =================================================================
def histori(mode,type,detail):
    df = pd.read_csv("histori.csv")
    if mode == "tambah":
        df = df.append(detail,ignore_index=True)
        df.to_csv("histori.csv",index=False)
    elif mode == "cari":
        if type == "produk":
            df = df[df['type'].str.contains(detail)]
        elif type == "dispatch":
            pass
    elif mode == "tampilkan":
        print(df)
        print(f"Jumlah Data :",df.shape[0])
    
# ================================================================================
def Mitra(user): 
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
            no_telp = input("Masukkan nomor telepon mitra : ")
            mitra = mitra.append(pd.Series({
                "id":mitra.shape[0]+1,
                "nama":nama,
                "alamat":alamat,
                "no_telp":no_telp
            }),ignore_index=True)
            mitra.to_csv("mitra.csv",index=False)
            print("Mitra berhasil ditambahkan")
        case "2":
            id = input("Masukkan id mitra : ")
            mitra = mitra[mitra['id'] != int(id)]
            mitra.to_csv("mitra.csv",index=False)
            print("Mitra berhasil dihapus")
        case "3":
            id = input("Masukkan id mitra : ")
            nama = input("Masukkan nama mitra : ")
            alamat = input("Masukkan alamat mitra : ")
            no_telp = input("Masukkan nomor telepon mitra : ")
            mitra = mitra[mitra['id'] != int(id)]
            mitra = mitra.append(pd.Series({
                "id":id,
                "nama":nama,
                "alamat":alamat,
                "no_telp":no_telp
            }),ignore_index=True)
            mitra.to_csv("mitra.csv",index=False)
            print("Mitra berhasil diedit")
            
def Dispatch(user):
    dfPegawai = pd.read_csv("users.csv")
    userole = dfPegawai[dfPegawai['username'] == user]['role'].values[0]
    username = dfPegawai[dfPegawai['username'] == user]['username'].values[0]
    if userole == "pegawai":
        pass
    if userole == "admin":
        print("Admin Dispatch")
        dfProduk = pd.read_csv("produk.csv")
        dfDispatch = pd.read_csv("dispatch.csv")
        dfMitra = pd.read_csv("mitra.csv")
        print(dfProduk.to_string(index=False))
        id_produk = input("Masukkan id produk yang akan didispatch : ")
        jumlah = input("Masukkan jumlah produk yang akan didispatch : ")
        print(dfMitra.to_string(index=False))
        mitra = input("Pilih mitra yang akan menerima dispatch (id) : ")
        print(dfPegawai[dfPegawai['role'] == "pegawai"][['id','username','role']].to_string(index=False))
        id_pegawai = input("Pilih pegawai yang akan melakukan dispatch (id) : ")
        
        DispatchDict = pd.Series({
            "id":dfDispatch.shape[0]+1,
            "id_pegawai":id_pegawai,
            "id_mitra":mitra,    
            "id_barang":id_produk,
            "jumlah":jumlah,
            "tanggal":time.strftime("%d/%m/%Y"),
            "jam":time.strftime("%H:%M:%S"),
            "status":"process"
        })
        print(DispatchDict)
        dispatch = dfDispatch._append(DispatchDict,ignore_index=True)
        dispatch.to_csv("dispatch.csv",index=False)
        
    
Dispatch("admin")