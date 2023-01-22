from mylib import *
from pathlib import Path
import os
import json


def add_app(exe, dirc):
    #esta zona vai adicionar o caminho do exe ao ficheiro json
    try:
        with open("programa/apps_roots.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
    data[exe] = dirc

    with open("programa/apps_roots.json", "w") as f:
        json.dump(data, f)
    #esta zona vai adicionar o nome da aplicação ao ficheiro json
    try: 
        with open("programa/apps_names.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
    data[exe] = [exe[0:-4]]
    with open("programa/apps_names.json", "w") as f:
        json.dump(data, f)


def get_apps_dir(caminho='.',idk=True):   # tem alguma coisa em erro !!! tenho de corrigir e melhorar o feacture da process bar  
    current_files = 0
    progress= 0
    for item in os.listdir(caminho): 
        if os.path.isfile(os.path.join(caminho, item)) and item.endswith('.exe'):
            add_app(item, (caminho+item))          
        if os.path.isdir(os.path.join(caminho, item)):  
            if 'logs' in item:
                pass                     
            try:                       
                get_apps_dir(os.path.join(caminho, item), False)
            except PermissionError:
                pass
                                
        
        if idk:            
            current_files +=1
            if (current_files*25/len(os.listdir(caminho))) != progress:
                progress = current_files*25/len(os.listdir(caminho))
                os.system('cls')
                print(progress,'% complete')
