string = " dumiLsion ddfd"


#upper - deixa a string em maiuscula
# lower oposto de upper
#capitalize - deixa a primiera letra em maiuscula

#isUpper verifica se esta tudo maiscula
#isLower
#strip - remove o espaço de uma string antes e depois do texto 
# replace - substitui uma string por outra 
# len gaz a contagem  de uma string 

# print(string.upper())
# print(string.lower())
# print(string.capitalize())
# print(string.isupper())
# print(string.strip())
# print(string.replace("d",' Deus ',1))

# #pegando o indice de uma string
# print(string[2])
# # pegando um intervalo
# print(string[2:6])

# in verifica se um texto existe em uma string

# retonando o index pelo texto 

string_code = input("Pesquise o index: ") 
x = string_code in string
if(x): 
    print(string.index(string_code))    
else:
    print("Texto não encontrado")
