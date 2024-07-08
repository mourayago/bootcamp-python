from utils import ler_csv, processar_dados, calcular_total_vendas

caminho_arquivo = "vendas.csv"

produtos = ler_csv(caminho_arquivo)
vendas = processar_dados(produtos)
vendas_cat = calcular_total_vendas(vendas)
print(vendas_cat)

