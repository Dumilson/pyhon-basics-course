# Exceção basica

try:
    numero = float(input("Informe um numero: "))
    # print(x)
    print(numero)
    # 10/0
except ZeroDivisionError:
    print("É impossivel dividir por zero")
except ValueError:
    10
    print("Valor invalido")
except:
    print("Erro inesperado")
finally:
    print("Sempre Executa")
