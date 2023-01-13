from mylib import *
from caminhos import *
import textwrap
import os


def add_app(exe, dirc):
    t1 = teste.copy()   
    t1.update({exe: dirc}) #update vai atualizar o caminho do exe, caso ele nao exista vai ser criado   

    with open('programa\\caminhos.py','w') as f:
        f.write("teste={")
        for i in t1:
            f.write(f"'{i}': '{t1[i]}',") 
        f.write("}")

def get_dir_size(path):
    total = 0
    with os.scandir(path) as it:      
        try:
            for entry in it:  # it = iterator it = os.scandir(path)                             
                if entry.is_file():
                    total += entry.stat().st_size                    
                elif entry.is_dir():
                    total += get_dir_size(entry.path)
        except NotADirectoryError:
            return os.path.getsize(path)
        except:
            pass
    return total

def get_apps_dir(item,caminho='.'): #vai procurar por aplicações
    try:        
        for i in range(0,len(os.listdir(caminho))):            
            os.system('cls')    
            for i in os.scandir(caminho):
                try:
                    if get_dir_size(i.path) > 1: # vai fazer a verificação de tamanho de cada pasta em bytes                  
                        #agora tenho de fazer a verificação de tamanho de len para evitar logs e executar o resto da função com esta nova implementação
                        print(i.path)
                        print(get_dir_size(i.path))
                except:
                    pass
            
            quit()        
            for x in range(0 , len(item)):                
                if os.listdir(caminho)[i] == item[x]:
                # if os.listdir(caminho)[i].endswitch('.exe') == True:  <-- vai guardar o caminho de todos os executaveis
                    add_app({os.listdir(caminho)[i] , caminho + '\\' + os.listdir(caminho)[i]})                                    
                else:                
                    if os.path.isdir(caminho + '\\'+ os.listdir(caminho)[i]) == True:
                        try:
                            get_apps_dir(item,caminho + '\\' + os.listdir(caminho)[i])
                        except:
                            print('erro ao entrar na pasta: ',caminho + '\\' + os.listdir(caminho)[i])
    except:
        pass
    print('done')

get_apps_dir('nada',get_first_dir(os.getcwd()))
