import pandas as pd
from datetime import datetime
import os
import logging

logging.basicConfig(level=logging.DEBUG, 
                    filename = "log.log", 
                    filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def ler_json(arquivo_json):
    df = pd.read_json(arquivo_json)
    logger.info(f"{arquivo_json} - arquivo lido com sucesso")
    return df

def list_files_dir(path: str) -> list:
    '''Passa um caminho de um diretório e retorna uma lista com todos os arquivos contidos'''
    arr = os.listdir(path)
    return arr

def inserir_datetime():
    current_dateTime = datetime.now().strftime("%Y-%m-%d %H:%M")
    return current_dateTime


def concatenar_dados(lista_arquivos: list) -> pd.DataFrame:
    pasta = 'data/'
    df_concatenado = pd.DataFrame()
    for arquivo in lista_arquivos:
        print('lendo',pasta+arquivo)
        df_temp = ler_json(pasta+arquivo)
        df_concatenado = pd.concat([df_temp,df_concatenado])
        print('ok')

    df_concatenado["inserted_at"] = inserir_datetime()
    return df_concatenado


def exportar_dados(dataframe):
    # flag
    # while flag != "csv" or flag != "parquet":
    try:
        flag = input("Deseja extrair em CSV ou Parquet?").lower().strip()
        if flag == "csv":
            dataframe.to_csv("vendas.csv")
            logger.info(f"arquivo salvo em csv - flag: {flag}")
        else:
            dataframe.to_parquet("vendas.parquet")
            logger.info(f"arquivo salvo em parquet - flag: {flag}")
    except:
        logger.error("Erro de seleção de arquivo",exc_info=True)

def run_pipeline(pasta: str) -> pd.DataFrame:
    '''Função utilizada para ler todos os arquivos .json de uma pasta, 
    concatenar os arquivos e salvar em um dataframe'''
    files = list_files_dir(pasta)
    df_final = concatenar_dados(files)
    print(df_final)
    exportar_dados(df_final)


if __name__ == "__main__":
    files = list_files_dir('data')
    print(files)
    df_final = concatenar_dados(files)
    print(df_final)
    exportar_dados(df_final)
    # print(concatenar_dados(files))

