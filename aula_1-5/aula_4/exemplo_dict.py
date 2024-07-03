from typing import Dict, Any

livro: Dict[str, Any] = {
    "livro": "Laranja Mecânica",
    "Autor": "Anthony Burgess",
    "Ano": 1962,
}

livro_2: Dict[str, Any] = {
    "livro": "Revolução dos Bichos",
    "Autor": "George Orwell",
    "Ano": 1945,
}

lista_livros = []
lista_livros.append(livro)
lista_livros.append(livro_2)
print(lista_livros)

lista_livros_dict = {livro,livro_2}
print(lista_livros_dict)


for k,v in livro.items():
    print(k,v)