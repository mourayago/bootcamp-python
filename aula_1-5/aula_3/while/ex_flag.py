#Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.


dados_users = []
flag =""

while flag.lower() != "!sair":
    nome=''
    dic_user = {}
    while True:
        try:
            nome = input("Qual o seu nome de usuário?")
            break
        except:
            print("Alguma coisa deu errado, tente novamente")

    dic_user["user"] = nome
    dados_users.append(dic_user)

    flag = input("Deseja adicionar mais pessoas? Caso não queira basta digitar !sair, caso queira digite SIM").lower()


print(dados_users)