import pandas as pd
from tabulate import tabulate
import os
import subprocess
def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None) 

def Update_produk():
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

Update_produk()