file = open(
    "/Users/snake/OneDrive/Documentos/GitHub/python-dio/05 - Manipulação de arquivos\lorem.txt", "r"
    )

file.readline() # lê o arquivo e retorna por linha
file.read() # lê o arquivo e retorna em string
file.readlines() # lê o arquivo e retorna uma lista com todas as linhas
file.close()