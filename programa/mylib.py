import os;
from exe_names import *

#esta função vai ser utilizada para tratar dos dados introduzidos pelo utilizador para entender que app o utilizador deseja executar
def get_exe(word): #retorna o .exe se encontrar um nome que correposda
    for app in dicionario:
        names = dicionario[app]
        for name in range( 0, len(names)):
            if str.upper(names[name]) == word.upper():
                return app
    return word


def get_first_dir(caminho): #vai retornar todos os caminhos até chegar ao disco raiz
    while caminho != os.path.dirname(caminho):
        caminho = os.path.dirname(caminho) 
    return caminho


# mudar o nome para abrir app ou algo assim pareciso e adicionar logoa questao do sinonimo
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




