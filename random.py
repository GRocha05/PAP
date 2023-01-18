def get_apps_dir(caminho='.'):   # tem alguma coisa em erro !!! tenho de corrigir e melhorar o feacture da process bar
    os.system('cls')    
    try:  
        
        
        quit()            
        for root, dirs, files in os.walk(caminho):   
            print(current_files*ptc/total_files, '%')
            current_files +=1             
            for file in files:
                if os.path.isfile(os.path.join(root, file)) and file.endswith('.exe'):
                    # add_app(file, (root+file))    
                    continue                                    
            for dir in dirs:
                if 'logs' not in dir:
                    current_files +=get_apps_dir(os.path.join(root, dir))                   
    except PermissionError:
        print(f"Erro ao entrar na pasta: {dir} por falta de permissão")
    except Exception as e:
        print(f"Erro ao entrar na pasta: {dir}\n{e}")
    return current_files
