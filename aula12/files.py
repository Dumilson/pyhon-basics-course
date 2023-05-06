

import os
# files = open("aula12/text.txt","r")
# files = open("aula12/textw.txt","w")
try:
    #Remover ficheiros
    # os.remove("aula12/uk_lits.xls")
    
    #Remover pasta só remove a pasta se estiver vazia
    
    
    os.rmdir("aula12/pasta")
    
    # Verifica se o arquivo pode ser lido 
    # files.readable()
    # print(files.read())
    # Tranforma os resltads em uma lista files.readlines()
    # Ler linhas  por linha files.readline
    # Adicionar dados no ficheirofiles.write()
    
    # files.write("JS \n")
    # files.write("PYTHON \n")
    # files.write("C# \n")
    # files.write("LARAVEL \n")
    # files.write("PYTHON 4 \n")
    
    # print(files.read())
    
    #verifica se o ficheiro existe
    # if(os.path.exists("aula12/text.txt")):
    #     print("Ficheiro  existe")
    # else: 
    #     print("Ficheiro não existe")
        
except Exception as e:
    print(e)
# finally:
# files.close()
# r  - leitura
# a  - incrimentar adiciona dados sem apagar o que existe no ficheiro
# w  - escrita adiciona dados mas apaga todas as informações que nele contem e se ele não encontrar o ficheiro para escrita ele cria um ficheiro novo
# x  - criar
# r+  - leitura mais escrta
