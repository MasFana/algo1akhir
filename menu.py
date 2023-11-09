import pandas as pd
import csv
import os
import subprocess
def Clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:  
        _ = subprocess.call('clear')


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

Menu(user="admin",role="admin")
