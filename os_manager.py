import os
import pandas as pd
class OSManager:

    def __init__(self):
        pass

    def clear_console_log(): #Clears console log
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_file_size(file): #Returns the filesize of a determined file
        if file == "categorias.csv":
            path = f"./SupuestosGenerales/Generales/Categorias/{file}"
            fileSize = os.path.getsize(f"{path}")
        
        return fileSize
    
    def create_directory(path):

        os.makedirs(os.path.dirname(path), exist_ok = True)

    def create_file(path, output = False): #Returns an opened file

        OSManager.create_directory(path)
        
        file = open(path,"a")


        if output == True:
            return file
        else:
            file.close()
        # return (os.path.getsize(f"{path}"))

    def open_pandas_csv_file(path):

        OSManager.create_file(path)

        pandasFile = pd.read_csv(path)
        
        return pandasFile
