import os
import datetime

class FilesProcessor():
    "Classe responsável pela leitura, tratamento e armazenamento de arquivos JSON e  TXT"
    def __init__(self, folder_path):
        self.folder_path = folder_path

def get_files(folder_path):
    '''Passa um caminho de um diretório e retorna uma lista com todos os arquivos contidos'''
    arr = os.listdir(folder_path)
    return arr

def check_files(folder_path) -> list:
    '''Faz um check da última modificação do arquivo alocados dentro de uma pasta
    e salva eles em uma lista'''
    files = get_files(folder_path)
    previous_files = []
    for file in files:
        file_value = {}
        unix_time = os.path.getmtime(folder_path + "\\" + file)
        file_last_update = datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
        file_value['file_name'] = file
        file_value['last_update'] = file_last_update
        print(file_value)
        print(previous_files.append(file_value))
    print(previous_files)
    
    

    
if __name__ == "__main__":
    folder_path = "C:\\Users\\Yago\\Documents\\Bootcamp Python\\bootcamp-python\\aula_11-15\\aula_13\\data\\json_files"
    #print(get_files(folder_path))
    check_files(folder_path=folder_path)


