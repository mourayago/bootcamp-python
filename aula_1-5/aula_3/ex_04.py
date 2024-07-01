import re

def is_valid_email(email):

    """Check if the email is a valid format."""

    # Regular expression for validating an Email

    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    # If the string matches the regex, it is a valid email

    if re.match(regex, email):

        return True

    else:

        return False

idade = int(input("Qual a sua idade?"))
email = input("Qual o seu email?")

if not 18 <= idade <= 65:
    print("Idade fora do range de idade")
elif is_valid_email(email) == False:
    print("por favor insira uma email válido")
else: 
    print("Dados de usuário válidos")

