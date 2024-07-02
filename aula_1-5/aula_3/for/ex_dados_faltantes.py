usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

# usuarios_nao_validos = []

# for usuario in usuarios:
#     if usuario["email"] == "":
#         usuarios_nao_validos.append(usuario["nome"])

# print(usuarios_nao_validos)

# for inline


usuarios_nao_validos = [usuario["nome"] for usuario in usuarios if usuario["email"] == ""]
print(usuarios_nao_validos)