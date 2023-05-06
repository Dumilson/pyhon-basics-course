pessoas = []

def add_pessoa(pessoa):
    return pessoas.extend(pessoa)

def listar_pessoa():
    return pessoas

def deletar(elemento):
    x = elemento in pessoas
    if(x):
      print("Eliminado!")
    else: 
      print("Não Encontrado !")
    