# Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.


idades = [22, 15, 30, 17, 18]
lista_maiores = [idade for idade in idades if idade > 18]

# for idade in idades:
#     if idade > 18:
#         lista_maiores.append(idade)

print(lista_maiores)