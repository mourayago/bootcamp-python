#Divisão de Dados em Grupos
#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [c for c in valores if c%2 == 0]
impares = [c for c in valores if c%2 != 0]

print(f"Lista de Pares {pares}")
print(f"Lista de Impares {impares}")