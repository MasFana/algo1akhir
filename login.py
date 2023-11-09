import pandas as pd
import os
import subprocess

def Clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:  
        subprocess.call('clear')

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
                Clear_terminal()
                return username
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

print(login())




