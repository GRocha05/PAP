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
