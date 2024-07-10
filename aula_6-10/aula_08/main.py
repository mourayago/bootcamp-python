from etl import ler_json, list_files_dir, concatenar_dados, exportar_dados


files = list_files_dir('data')
print(files)
df_final = concatenar_dados(files)
print(df_final)
exportar_dados(df_final)