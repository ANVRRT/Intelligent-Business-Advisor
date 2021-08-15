import os
import pandas as pd
class OSManager:

    def __init__(self):
        pass

    def clear_console_log(self): #Clears console log
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_file_size(self,file): #Returns the filesize of a determined file
        if file == "categorias.csv":
            path = f"./SupuestosGenerales/Generales/Categorias/{file}"
            fileSize = os.path.getsize(f"{path}")
        
        return fileSize
    
    def create_directory(self,path):

        os.makedirs(os.path.dirname(path), exist_ok = True)

    def create_file(self, path, output = True): #Returns an opened file

        self.create_directory(path)
        
        file = open(path,"a")


        if output == True:
            return file
        else:
            file.close()
        # return (os.path.getsize(f"{path}"))

    def open_pandas_csv_file(self, path):

        self.create_file(path, output = False)

        pandasFile = pd.read_csv(path)
        
        return pandasFile
