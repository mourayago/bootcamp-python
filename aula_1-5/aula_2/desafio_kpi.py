
try:
    nome_usuario = input("Qual o o seu nome?")
except Exception as e:
    print('Alguma coisa deu errado tente novamente')
    print(e)

if nome_usuario.isdigit() == True:
    while nome_usuario.isdigit() == True:
        nome_usuario = input('O nome do seu usuário não pode contar números, por favor digite novamente')
elif len(nome_usuario) == 0:
    while len(nome_usuario) == 0:
        nome_usuario = input('O nome do seu usuário não pode estar vazio, por favor digite novamente')
elif nome_usuario.isspace() == True:
    while nome_usuario.isspace() == True:
        nome_usuario = input('Digite novamente o seu nome de usuário')
else:
    pass


while True:
    try: 
        salario = float(input("Qual o seu salário mensal? ex: 2500.50 "))
        break
    except ValueError:
        print('Valor de salário digitado de forma errada, pfvr repetir o processo')
    

while True:
    try: 
        percent_bonus = float(input("Seu '%' de  de bonus:"))
        break
    except ValueError as e:
        error = str(e)
        if "string to float: ''" in error:
            print('Caso seu "%" seja zero, por favor digitar 0')
        if "%" in error:
            print('Digite o seu número sem o % no inicio ou no final')
        
bonus = salario * (1+(percent_bonus/100))
apuracao = salario + bonus

print(f"Olá {nome_usuario}, o seu bônus foi de R$ {bonus} o seu recebimento mensal será de R$ {apuracao}")