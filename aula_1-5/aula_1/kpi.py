#Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome_usuario = input("Qual o o seu nome?")
salario = float(input("Qual o seu salário mensal? ex: 2500.50 "))
percent_bonus = float(input("seu '%' de  de bonus:"))

print(1+percent_bonus/100)
bonus = salario * (1+(percent_bonus/100))
apuracao = salario + bonus

print(f"Olá {nome_usuario}, o seu bônus foi de R$ {bonus} o seu recebimento mensal será de R$ {apuracao}")