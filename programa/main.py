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

overlay =  overlay() # cria o objeto de sobreposição


overlay.abrir()
# quando a sobrepossição é chamada

def funcao():
    print('teste')
    root.destroy()

funcao()

quit()

# tenho de entender como funciona esta função e criar a minha propria função para verificar o tamanho de um ficheiro ou pasta
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

# ---------------------------------------------------------------

for i in range(0, len(os.listdir(recursividade(os.getcwd())))):
    if os.path.isdir(recursividade(os.getcwd()) + '\\' + os.listdir(recursividade(os.getcwd()))[i]) == True:
        print('pasta',os.listdir(recursividade(os.getcwd()))[i])
        try:
            print(get_dir_size(recursividade(os.getcwd()) + '\\' + os.listdir(recursividade(os.getcwd()))[i]))
        except:
            print('erro a opter o tamanho do ficheiro')


# ---------------------------------------------------------------

quit()
print(os.listdir(os.getcwd()))
print(os.getcwd())
print(os.path.getsize(os.getcwd()))


quit()


print(os.stat(os.getcwd()))


quit()

# fazer um ficheiro de python proprio para os caminhos e para os .exe 
# adiciona na lista normalmente em codigo, e depois substitui no ficheiro atraves de ler e escrever do python
"""
ex: 
ficheiro:
    dicionario =
    {
    'chrome.exe' : ['chrome','google','google chrome'],
    'Teste' : ['idk','okig']
    }
python:
    dicionario[teste].append = 'talvez'
    
ficheiro depois de python:
    dicionario =
    {
    'chrome.exe' : ['chrome','google','google chrome'],
    'Teste' : ['idk','okig','talvez']
    }    


"""



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


