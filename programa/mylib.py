import os;
from dicionario import *
apps = {}


#esta função vai ser utilizada para tratar dos dados introduzidos pelo utilizador para entender que app o utilizador deseja executar
def sinonimos(word): #retorna o nome da variavel e de algum sinonimo existente
    for app in dicionario:
        sinonimos = dicionario[app]
        for sinonimo in range( 0, len(sinonimos)):
            if str.upper(sinonimos[sinonimo]) == word.upper():
                return app
    return word


def recursividade(caminho): #vai retornar todos os caminhos até chegar ao disco raiz
    while caminho != os.path.dirname(caminho):
        caminho = os.path.dirname(caminho) 
    return caminho


def procura_app(item,caminho):
    try:        
        for i in range(0,len(os.listdir(caminho))):            
            os.system('cls')
            print('loops feitos: ',i)
            print('caminho: ',caminho)
            for x in range(0 , len(item)):                
                if os.listdir(caminho)[i] == item[x]:
                # if os.listdir(caminho)[i].endswitch('.exe') == True:  <-- vai guardar o caminho de todos os executaveis
                    apps.update({os.listdir(caminho)[i]:caminho + '\\' + os.listdir(caminho)[i]})                                    
            else:                
                if os.path.isdir(caminho + '\\'+ os.listdir(caminho)[i]) == True:
                    try:
                        procura_app(item,caminho + '\\' + os.listdir(caminho)[i])
                    except:
                        print('erro ao entrar na pasta: ',caminho + '\\' + os.listdir(caminho)[i])
    except:
        pass
    print('done')
    return apps


def abrir(item, caminhos):
    try:
        os.startfile(caminhos[item])
    except:
        print('app nao encontrada')
            

# Na função abrir 


# fazer filtragem de pastas que a função vai ou nao entrar(maximo de itens aceitaveis)
# em cima esta em stand by


# fazer função para abrir as aplicacoes



# verificar se os ficheiros mais visitados/abertos pelo utilizador


# fazer a sobrepossição no monitor

# ------------------------------------------------------------------------------------------

# Organização das funções


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








"""






