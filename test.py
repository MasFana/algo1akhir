
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
def Mitra(): 
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
            newMitra = pd.DataFrame({
                "id":[mitra.shape[0]+1],
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
            nama = input("Masukkan nama mitra : ")
            alamat = input("Masukkan alamat mitra : ")
            mitra = mitra.append(pd.Series({
                "nama":nama,
                "alamat":alamat,
            }),ignore_index=True)
            mitra.to_csv("mitra.csv",index=False)
            print("Mitra berhasil diedit")
            
def Dispatch(user):
    dfPegawai = pd.read_csv("users.csv")
    userole = dfPegawai[dfPegawai['username'] == user]['role'].values[0]
    username = dfPegawai[dfPegawai['username'] == user]['username'].values[0]
    if userole == "pegawai":
        print("Pegawai Dispatch")
        dfDispatch = pd.read_csv("dispatch.csv")
        print(dfDispatch[dfDispatch['id_pegawai'] == username].to_string(index=False))
        id_dispatch = input("Masukkan id dispatch yang sudah selesai : ")
        dfDispatch.loc[dfDispatch['id'] == int(id_dispatch),'status'] = "selesai"
        
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
            "status":"proses"
        })
        print(DispatchDict)
        dispatch = dfDispatch._append(DispatchDict,ignore_index=True)
        dispatch.to_csv("dispatch.csv",index=False)
        
Mitra()