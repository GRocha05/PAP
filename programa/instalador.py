from mylib import *
from pathlib import Path
from caminhos import *
import textwrap
import os
import json



def add_app(exe, dirc):
    try:
        with open("programa/caminhos.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
    data[exe] = dirc

    with open("programa/caminhos.json", "w") as f:
        json.dump(data, f)

# esta função é para ser usada no mylib
def get_app_path(exe):
    try:
        with open("programa/caminhos.json", "r") as f:
            data = json.load(f)
            return data[exe]
    except (FileNotFoundError, json.decoder.JSONDecodeError, KeyError):
        return None


def get_apps_dir(caminho='.', total_files=0, current_files=0):   # tem alguma coisa em erro !!! tenho de corrigir e melhorar o feacture da process bar
    os.system('cls')    
    ptc= 100
    try:              
        for root, dirs, files in os.walk(caminho):   
            print(current_files*ptc/total_files, '%')
            current_files +=1             
            for file in files:
                if os.path.isfile(os.path.join(root, file)) and file.endswith('.exe'):
                    # add_app(file, (root+file))    
                    continue                                    
            for dir in dirs:
                if 'logs' not in dir:
                    current_files +=get_apps_dir(os.path.join(root, dir))                   
    except PermissionError:
        print(f"Erro ao entrar na pasta: {dir} por falta de permissão")
    except Exception as e:
        print(f"Erro ao entrar na pasta: {dir}\n{e}")
    return current_files


total_files = sum([len(files) for r, d, files in os.walk(get_first_dir(os.getcwd()))])

teste= get_apps_dir(get_first_dir(os.getcwd()), total_files=total_files)
print("terminado")
print(teste*100/total_files, '%')


quit()
global app

def add_app(exe, dirc):
    try:
        t1 = teste.copy()  
    except NameError:
        t1 = {} 
    t1.update({exe: dirc}) #update vai atualizar o caminho do exe, caso ele nao exista vai ser criado   

    with open('programa\\caminhos.py','w') as f:
        f.write("teste={")
        for i in t1:
            f.write(f"'{i}': '{t1[i]}',") 
        f.write("}")

def get_apps_dir(item='.', caminho='.',app=0):
    os.system('cls')
    try:
        for root, dirs, files in os.walk(caminho):            
            print(root)            
            for file in files:
                # if file in item:                
                if file.endswith('.exe'):
                    print('encontrado: ', file)  
                    print('caminho: ', root)
                    
                    app += 1                  
                    add_app(file, root)
            for dir in dirs:              
                try:
                    get_apps_dir(item, dir, app)
                except:
                    print('erro ao entrar na pasta: ', dir)
    except:
        pass
    

    

get_apps_dir(caminho=get_first_dir(os.getcwd()))
print('fim')
print('foram encontradas: ', app, 'aplicacoes')