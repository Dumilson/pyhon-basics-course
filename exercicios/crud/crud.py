import db

op = 0

global nome

while (op == 0):
    action = int(input("Escolha uma opção\n1 - Adicionar \n2 - Listar \n3- Deletar"))
    match action:
        case 1:
            nome = input("Informe o nome: ")
            db.add_pessoa([nome])
        case 2:
            print(db.listar_pessoa())
        case 3:
            print(db.listar_pessoa())
            nome = input("Qual Usuario quer eliminar (Escreva o nome): ")
            print(db.deletar(nome))
        case _:
          print("Opção invalida")
    op = int(input("0 - Continuar \n1 - Sair \n"))

print("Saiu da Aplicação todos os seus dados foram perdidos")
