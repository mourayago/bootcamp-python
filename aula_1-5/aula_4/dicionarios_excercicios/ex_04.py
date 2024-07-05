# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario = {"a": 1, "b": 2, "c": 3}

lista_chaves = [k for k in dicionario.keys()]
lista_valores = [v for v in dicionario.values()]

print(lista_chaves)
print(lista_valores)