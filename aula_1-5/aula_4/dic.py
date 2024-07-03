import json 


produto_1 = {
    "nome" : "Sapato",
    "quantidade" : 10,
    "preco" : 70.3,
    "disponibilidade" : True
}

produto_2 = {
    "nome" : "Camisa",
    "quantidade" : 5,
    "preco" : 199,
    "disponibilidade" : True
}

carrinho: list = []

carrinho.append(produto_1)
carrinho.append(produto_2)

carrinho_json = json.dumps(carrinho)

print(carrinho)
print(carrinho_json)

print(type(carrinho))
print(type(carrinho_json))




