import pandas as pd
import os

def ler_json(arquivo_json):
    df = pd.read_json(arquivo_json)
    return df

def list_files_dir(path: str) -> list:
    '''Passa um caminho de um diretório e retorna uma lista com todos os arquivos contidos'''
    arr = os.listdir(path)
    return arr

def concatenar_dados(lista_arquivos: list):
    pasta = 'data/'
    df_concatenado = pd.DataFrame()
    for arquivo in lista_arquivos:
        print('lendo',pasta+arquivo)
        df_temp = ler_json(pasta+arquivo)
        df_concatenado = pd.concat([df_temp,df_concatenado])
        print('ok')
    return df_concatenado

def exportar_dados(dataframe):
    # flag = ''
    # while flag != "csv" or flag != "parquet":
    flag = input("Deseja extrair em CSV ou Parquet?").lower().strip()
    if flag == "csv":
        dataframe.to_csv("vendas.csv")
    else:
        dataframe.to_parquet("vendas.parquet")


if __name__ == "__main__":
    # data_json = ler_json('data/coleta_dia01.json')
    # print(data_json)
    files = list_files_dir('data')
    print(files)
    df_final = concatenar_dados(files)
    print(df_final)
    exportar_dados(df_final)
    # print(concatenar_dados(files))


    #TERMINAR A PARTE de LOG