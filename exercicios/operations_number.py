
n1 = float(input("Informe o numero 1: \n"))
n2 = float(input("Informe o numero 2: \n"))
n3 = float(input("Informe o numero 3: \n"))

def menor(n1,n2,n3):
        print(f" {max([n1,n2,n3])} é maior")
        print(f" {min([n1,n2,n3])} é menor")
    # if(n1 <= n2 and n1 <= n3):
    #     print(f" {n1} é menor")
    # elif(n2 <= n1 and n2 <= n3):
    #     print(f" {n2} é menor")
    # else:
    #     print(f" {n3} é menor")
    
    # if(n1 >= n2 and n1 >= n3):
    #     print(f" {n1} é maior")
    # elif(n2 >= n1 and n2 >= n3):
    #     print(f" {n2} é maior")
    # else:
    #     print(f" {n3} é maior")
    
print(f" {menor(n1,n2,n3)} ")

    