



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