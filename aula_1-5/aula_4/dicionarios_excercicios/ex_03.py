
#13. Filtragem de Dados em Dicionário
#Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.


estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_filtrado = {}

for k,v in estoque.items():
    if v > 0:
        estoque_filtrado[k] = v

print(estoque_filtrado)