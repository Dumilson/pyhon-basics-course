 # collection 
 # list são arrays 
 # truple  - () Lista imutavel 
 # set
 # insert - inseri um elemento em uma coleção escolhendo a posição 
 # pop - removo o ultimo valor 
 # pop(index) especcificando o index a remover 
 # remove - Remove a primiera ocorrencia dentro de um array 
 
 
 
 #se quer pegar o valor de uma lista de traz  para frente é só usar o -
 
familia = ["Eu", "Code", "Nana"]
# sonhos = {"nome", "Ser Rico"}

#modificando o valor do indece
# familia[1] = "Fredi"
# print(familia[0:2])

# familia.extend([sonhos])
# familia.append(["Teste","Looper"])
# familia.extend(["Code","Junior"])
# familia.insert(0,"texto")
# familia.pop(1)
# familia.remove("texto")

#ordernar a lista de forma crescente
#familia.sort()

#Oposto de Sorte
# familia.reverse()

# Referencia de variavel 
# familia2 = familia

#Guardar uma copia 
familia2 = familia.copy()

print(familia2)
familia.remove("Code")
print(familia2,familia)

# print(familia)
# for i in range(2):
#     print(familia[i])
# print(familia[2][0:2][0])
