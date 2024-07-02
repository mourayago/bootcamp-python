pagina_atual = 1
paginas_totais = 20

while pagina_atual <= paginas_totais:
    # for pagina in range(1,paginas_totais+1):
    #     print(f"Página numero {pagina}")
    #     pagina_atual += 1
    # print("leitura completa")

    #solução aula + prática
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print("Todas as páginas foram processadas.")