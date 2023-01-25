import os
from mylib import *
os.system('cls')

# os.path.isdir = verifica se é um diretorio
# os.listdir = lista os arquivos e diretorios
# os.lidir(local)[0] = lista o primeiro arquivo ou diretorio
# os.getcwd() = retorna o caminho atual
# os.getcwd() + '\\' + os.listdir(teste)[0] = retorna o caminho atual + o primeiro arquivo ou diretorio
# o de cima permite entrarmos nas pastas disponiveis
# para verificar algo sobre um ficheiro/diretoria tenho de adicionar o nome ao caminho atual e verificar, exemplo
# na pasta programa tenho um ficheiro chamado google, para verificar se é um ficheiro ou app tenho de entrar no programa/google e depois verificar




quit()

# fazer um ficheiro de python proprio para os caminhos e para os .exe 
# adiciona na lista normalmente em codigo, e depois substitui no ficheiro atraves de ler e escrever do python



#em baixo é um pseudo do return da procura_app
teste={'cpuz.exe': 'C:\\\\Program Files\\CPUID\\CPU-Z\\cpuz.exe', 'chrome.exe': 'C:\\\\Program Files\\Google\\Chrome\\Application\\chrome.exe'}

#teste de app escolhida para ser executada
app = 'chrome'
# essa função tera de verificar se o nome da aplicação existe no dicionario, verificar os sinonimos da aplicação e depois abrir a aplicação
# caso seja sinonimo, vai abrir a aplicação respetiva, caso contrario vai tentar abrir a aplicação atraves do nome colocado pelo utilizador

abrir(sinonimos(app),teste)


quit()

idk =['chrome.exe','Muck.url','cpuz.exe']

caminhos = procura_app(idk,recursividade(os.getcwd()) + '\\' +'Program Files')

print(caminhos)

# tenho de fazer uma dicionario para tentar fazer a função de abrir as aplicações onde vai buscar o caminho atraves do nome da aplicação


