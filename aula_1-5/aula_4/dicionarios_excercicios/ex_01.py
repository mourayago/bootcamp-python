#11. Atualização de Dados
#Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

lista_produtos = []

for produto in produtos:
    lista_produtos.append(produto["nome"].lower())

while True:
    try:
        produto_select = input(f"Qual produto você deseja atualizar o preço? {lista_produtos}").strip().lower()
        while produto_select not in lista_produtos:
            print("produto não está na lista cadastrada, tente novamente.")
            produto_select = input(f"Qual produto você deseja atualizar o preço? {lista_produtos}").strip().lower()
        break
    except:
          print("algo deu errado tente novamente")  



for produto in produtos:
    if produto["nome"].lower() == produto_select:
        while True:
            try:
                produto["preço"] = float(input(f"Digite o novo preço do {produto_select}?"))
                break
            except:
                print("algo deu errado tente novamente")


print("Catalogo de produtos atualizado!")
print(produtos)