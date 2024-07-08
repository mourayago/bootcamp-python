# Vamos revisar funções adicionando type hints e Pydantic

# 1. Calcular Média de Valores em uma Lista

from typing import List

def media_lista(lista: List[float]) -> float:
    '''Recebe uma lista de valores e retorna a média dela'''
    sum = 0
    tam = len(lista)
    for v in lista:
        sum = sum+v    
    media = sum/tam
    return  media


if __name__ == "__main__":

    lista_valores = [20.5 , 10, 33.3, 50]
    med_list = media_lista(lista_valores)
    print(med_list)