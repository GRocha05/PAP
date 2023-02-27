
# print(os.getenv('Username')) <-- vai buscar o nome do utlizador que está a utilizar o computador
import os
import json
import importlib.util
import subprocess
import tkinter as tk
from tkinter import filedialog 

global root

def janela():
    root = tk.Tk()
    root.withdraw()


#função para importar a as bibliotecas caso nao sejam encontradas no computador
def import_module(name):
    spec = importlib.util.find_spec(name)
    if spec is None:
        # The module does not exist, install it
        subprocess.run(["pip", "install", name])
        spec = importlib.util.find_spec(name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

try:
    import Levenshtein
except ModuleNotFoundError:
    import_module("Levenshtein")

class EmptyError(Exception):
    "exe ou dirc vazio"
    pass


def add_app(exe, dirc):
    if exe == "" or dirc == "":
        raise EmptyError()
    if not os.path.exists(dirc):
        raise FileNotFoundError()
    if not os.path.isfile(dirc):
        raise NotADirectoryError()
    dirc = dirc.replace('"', '') # vai evitar erros ao guardar o caminho no ficheiro json
    exe= exe.replace('"', '') 
    exe= exe.replace("\\", "")
    if os.path.islink(dirc): #caso o caminho seja um atalho vai ser convertido para o caminho do exe
        dirc = os.readlink(dirc)
    #esta zona vai adicionar o caminho do exe ao ficheiro json
    try:
        with open("programa/apps_paths.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
    data[exe] = dirc

    with open("programa/apps_paths.json", "w") as f:
        json.dump(data, f)
    #esta zona vai adicionar o nome da aplicação ao ficheiro json
    try: 
        with open("programa/apps_names.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
    data[exe] = [exe.replace(".exe", "")]
    with open("programa/apps_names.json", "w") as f:
        json.dump(data, f)


#função que vai o caminho raiz do disco
def get_first_dir(caminho): #vai retornar todos os caminhos até chegar ao disco raiz
    while caminho != os.path.dirname(caminho):
        caminho = os.path.dirname(caminho) 
    return caminho

def compare_words(word1, word2):
    distance = Levenshtein.distance(word1, word2)
    if distance <= 2:
        return True
    else:
        return False
 

#esta função vai ser utilizada para tratar dos dados introduzidos pelo utilizador para entender que app o utilizador deseja executar
def get_exe(word): #retorna o .exe se encontrar um nome que correposda
    try:
        #vai abrir o ficheiro json e verificar se o nome introduzido pelo utilizador corresponde a algum nome de uma aplicação
        with open("programa/apps_names.json", "r") as f:
            data = json.load(f)
            for exe in data:
                if word in data[exe]: # verifica se o nome está associado a algum exe no ficheiro
                    return exe 
            #caso o return seja executado é porque nao encontrou o nome na lista e termina a funcão
            #caso o return nao seja executado a função vai continuar e vai comparar as palavras no dicionario para 
            #procurar por palavras parecias e perguntar ao utlizador se por acaso se enganou
            for exe in data:
                for name in data[exe]:
                    if compare_words(word, name): # caso a função de comparar palavras retorne true vai confirmar se é esse o exe desejado
                        ask = input(f'quer dizer {name}? (y/n): ')
                        if ask == 'y': #caso seja o exe desejado vai adicionar o nome ao ficheiro json e dar return do exe corretamente
                            with open("programa/apps_names.json", "w") as f:
                                data[exe].append(word)
                                json.dump(data, f)                                
                            return exe                               
                    
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}
        with open("programa/apps_names.json", "w") as f:
            json.dump(data, f)
        return None      
    

def open_app(app=""):
    #caso nenhuma função seja executada o codigo vai continuar a executar até chegar ao final 
    #quando chegar ao final é porque nao encontrou nenhuma aplicação ou pasta e vai
    #perguntar se o utilizador quer adicionar manualmente
    if get_exe(app) != None:
        print("vai procurar nas aplicações")
        try:            
            os.startfile(app)
            print('aplicação aberta')
                
        except FileNotFoundError:
            try:
                with open("programa/apps_paths.json", "r") as f:
                    data = json.load(f)
                    if os.access(data[get_exe(app)], os.X_OK):
                        print("Executando a Aplicaçao")
                        os.startfile(data[get_exe(app)])
                        exit()# se executar vai terminar o if
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = {}
                with open("programa/apps_paths.json", "w") as f:
                    json.dump(data, f)
            except KeyError:
                pass
        
    print("Fazer função de procura nos recent")

    print('Aplicação nao encontrada')
    janela()
    ask = input('quer adicionar manualmente? (y/n): ')
    if ask != 'y':     
        exit()  
    path = ""
    try:
        path = filedialog.askopenfilename(initialdir = "c:\\", title = "Select file", filetypes = (("executable files", "*.exe*"), ("all files", "*.*")))
        add_app(os.path.basename(path), path)
        os.startfile(path)
        print("Aplicaçao adicionada com sucesso")
        return
    except EmptyError:
        print("Nenhum ficheiro foi selecionado")    
    except FileNotFoundError:
        print("Ficheiro não encontrado")
    except NotADirectoryError:
        print("O formato de caminho não é válido")
    except PermissionError:
        print("Não tem permissão para abrir o ficheiro")
    print("ocorreu algum erro")

open_app('arduino')

