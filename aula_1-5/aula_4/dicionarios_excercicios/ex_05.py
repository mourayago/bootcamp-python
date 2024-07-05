# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
texto_trado = texto.replace(" ","")
caracteres = {}

for c in texto_trado:
    if c in caracteres:
        caracteres[c] +=1
    else:
        caracteres[c] = 1

print(caracteres)