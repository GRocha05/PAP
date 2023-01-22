import os
import json
import Levenshtein

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
    
    

'''
No abrir a aplicação é suposto ver se ha o exe e se é possivel 
executar, caso nao encontre o caminho vai perguntar se quer adicionar 
manualmente
'''


#função para abrir aplicaçoes
def open_app(exe):
    
    if get_exe(exe) == None:
        try:
            print('vamos procurar nos recent uma pasta que verifique o nome')
        except Exception as e:
            print('nao foi possivel abrir a pasta desejada. erro {e}')
            
    
    elif get_exe(exe) != None:
        print('vamos procurar o caminho do exe')



# verificar se os ficheiros mais visitados/abertos pelo utilizador



# ------------Audio-----------

# captar o audio do microfone


# tratar o audio do microfone





# ------------overlay-----------

  
            





# ------------funções-----------

#- funções no pc:

# --Abrir aplicação
# --Procurar aplicação
# --procurar as pastas mais utilizadas(verificar se possivel!!)
# --Desligar/suspender e reniciar o pc



#- spotify:






"""
Links:

--Voz:
https://www.youtube.com/watch?v=mYUyaKmvu6Y&ab_channel=freeCodeCamp.org
https://www.youtube.com/watch?v=PWVH3Vx3dCI&ab_channel=Simplilearn
https://www.youtube.com/watch?v=zqEoTxkh95M&ab_channel=TechWithTim
https://www.youtube.com/results?search_query=know+you+speech+recognition+works
https://www.youtube.com/watch?v=bfmFfD2RIcg&ab_channel=Simplilearn
https://www.simplilearn.com/pgp-ai-machine-learning-certification-training-course?utm_campaign=NLPin5MinsScribe&utm_medium=Description&utm_source=youtube

--Overlay:
https://www.youtube.com/watch?v=zWuuk_j1iwM&ab_channel=tylerlaceby
https://www.youtube.com/results?search_query=create+a+transparent+app
https://www.youtube.com/watch?v=RqgsGaMPZTw&ab_channel=CodeMonkey
https://www.youtube.com/results?search_query=create+desktop+widets+with+python
https://www.youtube.com/watch?v=Pk9kRWcbJwE&ab_channel=MelvinChia


--spotify:
https://www.google.com/search?q=spotify+app&rlz=1C1VDKB_pt-PTPT1020PT1020&oq=spotify+app&aqs=chrome..69i57j0i512l6j69i61.2184j0j7&sourceid=chrome&ie=UTF-8
https://www.youtube.com/results?search_query=create+a+spotify+app+python
https://www.youtube.com/watch?v=c5sWvP9h3s8&ab_channel=ImdadCodes
https://www.youtube.com/watch?v=-FsFT6OwE1A&t=152s&ab_channel=EuanMorgan
https://www.youtube.com/watch?v=xdq6Gz33khQ&ab_channel=CodingEntrepreneurs





"""


# neural network
# https://www.youtube.com/watch?v=aircAruvnKk&ab_channel=3Blue1Brown
# https://www.youtube.com/watch?v=IHZwWFHWa-w&ab_channel=3Blue1Brown




