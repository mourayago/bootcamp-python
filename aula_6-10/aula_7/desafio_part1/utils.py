import csv


def ler_csv(path: str) ->list:
    lista = []
    with open(path, "r",encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha) 
    return lista

def processar_dados(lista: list) -> dict:
    totais_por_categoria = {}

    for produto in lista:
        categoria = produto['Categoria']
        quantidade = int(produto['Quantidade'])
        venda = int(produto['Venda'])
        
        if categoria not in totais_por_categoria:
            totais_por_categoria[categoria] = {'Quantidade': 0, 'Venda': 0}
        
        totais_por_categoria[categoria]['Quantidade'] += quantidade
        totais_por_categoria[categoria]['Venda'] += venda

    return totais_por_categoria

def calcular_total_vendas(vendas: dict) -> dict:
    vendas_categoria = {}

    for k,v in vendas.items():
        categoria = k
        quantidade = v["Quantidade"]
        venda = v["Venda"]
        total_vendas = quantidade * venda

        if categoria not in vendas_categoria:
            vendas_categoria[categoria] = 0

        vendas_categoria[categoria] = vendas_categoria[categoria] + total_vendas

    return vendas_categoria 


if __name__ == "__main__":
    #Lendo o CSV
    produtos = ler_csv("vendas.csv")
    #Agrupando as vendas por categoria no dicionário
    vendas = processar_dados(produtos)
    #Calculando o total de vendas do dicionárii
    vendas_cat = calcular_total_vendas(vendas)
    print(vendas_cat)

