#Ordenação Personalizada
#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

def get_pessoa_dict(lista: list):
    return lista["nome"]

pessoas[0]

#utilizando função lamba
#pessoas.sort(key=lambda pessoa: pessoa["nome"], reverse=True)


print(pessoas)

