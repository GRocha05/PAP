



quit()
import ctypes
import sys
import subprocess

# este ficheiro está a ser utilizado para fazer testes para opter acesso aos ficheiros do recent
# e ultrapasasr o problema de permissões negadas

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code to run with administrator privileges
    print("Running as administrator")
else:
    # Re-run the script with administrator privileges
    args = ["runas", "/user:Administrator", sys.executable] + sys.argv
    subprocess.run(args)



quit()
directory = 'C:\\Users\\Utilizador\\Recent'
permissions = 'Everyone:F'

os.system('icacls {} /grant {}'.format(directory, permissions))
files = os.listdir(directory)
print(files)



quit()



teste = ('C:\\Users\\Utilizador\\Recent')
os.chmod(teste, 755)
print(os.listdir(teste))