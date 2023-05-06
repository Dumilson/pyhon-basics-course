pessoas = [
    {
        "nome": "domingos",
        "idade": 10
    },
     {
        "nome": "Pipoca",
        "idade": 140
    }
]
pessoas.append({
        "nome": "Branca",
        "idade": 140
    })

for item in pessoas:
    print(f"Nome: {item['nome']} ")
    print(f"Idade: {item['idade']} \n")
