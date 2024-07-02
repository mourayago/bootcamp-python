texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
id_palavra = {"raposa":2,"cachorro":3,"o":1}
cont = 0
cont_id = 0
sum_pont = 0



for palavra in palavras:
    cont = cont + 1
    if palavra in id_palavra:
        print(f"'{palavra}' palavra reservada!")
        cont_id += 1
        sum_pont = sum_pont + id_palavra[palavra]
    
print(f"A frase contem um total de {cont} palavras, sendo {cont_id} reservada no dic")
print(f"A soma da pontuação das palavras reservadas foi de {sum_pont}")
