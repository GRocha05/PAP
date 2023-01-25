from mylib import *
from pathlib import Path
import os
import json



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
