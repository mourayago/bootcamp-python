
def contains_number(string):
    return any(string.find(str(i)) != -1 for i in range(10))

while True:
    # inserindo nome
    try:
        nome = input("digite o seu nome:")
        while True:
            if contains_number(nome) == True:
                nome = input("seu nome não pode conter dígitos, digite novamente")
            elif len(nome) == 0:
                nome = input("você não digitou um nome, digite novamente")
            elif nome.isspace() == True:
                nome = input("você digitou apenas espaços no nome, digite novamente")
            else:
                break 
    except:
        print("algo deu errado digite novamente")

    # inserindo salario
    while True:
        try: 
            salario = float(input("Qual o seu salário mensal? ex: 2500.50 "))
            break
        except ValueError:
            print('Valor de salário digitado de forma errada, pfvr repetir o processo')

    # inserindo percentual de bonus
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
    break

bonus = salario * (1+(percent_bonus/100))
apuracao = salario + bonus

print(f"Olá {nome}, o seu bônus foi de R$ {bonus} o seu recebimento mensal será de R$ {apuracao}")