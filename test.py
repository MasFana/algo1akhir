from ast import Lambda
import time
import pandas as pd
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
