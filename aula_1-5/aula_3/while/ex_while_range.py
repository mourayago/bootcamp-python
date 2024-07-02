num = int(input("digite um número entre o intervalo de 1 e 10"))

while num < 1 or num > 10:
    print("Número fora do intervalo!")
    num = int(input("Por favor, digite um número entre 1 e 10: "))

print("Número válido!")