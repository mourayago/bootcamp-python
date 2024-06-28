

try: 
    num_1 = int(input("Digite um número inteiro"))
    num_2 = int(input("Digite outro número inteiro"))
    soma = num_1 + num_2
    print(soma)
except Exception as e:
    print(e)
else:
    print('se der cert=o faz isso aqui tbm')
finally:
    print('indenpendente do que acontecer faz isso aqui tbm')

