import pandas as pd
from tabulate import tabulate
import os
import subprocess
def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')
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
Cari_produk()
    