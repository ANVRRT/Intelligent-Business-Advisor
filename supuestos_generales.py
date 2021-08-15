from input_manager import InputManager
from os_manager import OSManager
import pandas as pd
import numpy as np


class SupuestosGenerales:

    def __init__(self):
        pass

    def grabar_archivo(self,fileName, file,data):
        if fileName == "categorias.csv":
            
            if (OSManager().get_file_size(fileName) == 0):
                initialRegistry = "CATEGORIA" + "," + "J1" + "," + "J2" + "\n"
                file.write(initialRegistry)
                file.close()
            
            pandasFile = OSManager().open_pandas_csv_file(file.name)
            registry = pd.DataFrame({
                                    "CATEGORIA": [len(pandasFile.index)+1],
                                    "J1": [data[0]],
                                    "J2": [data[1]]
                                    })
            # print(pandasFile)
        pandasFile = pandasFile.append(registry)
        pandasFile.to_csv(file.name, index = False)

            # print(pandasFile)

                
            

    def agregar_categoria(self, J1, J2):
        
        # file = open("./SupuestosGenerales/Generales/Categorias/categorias.csv","a")
        fileName = "categorias.csv"
        data = [J1,J2]
        file = OSManager().create_file(f"./SupuestosGenerales/Generales/Categorias/{fileName}")

        # file = OSManager().open_pandas_csv_file(f"./SupuestosGenerales/Generales/Categorias/{fileName}")
        self.grabar_archivo(fileName,file,data)



# <-------------------------------------- STARTS SIMPLE TESTING REGION -------------------------------------------->
# <-------------------------------------- STARTS SIMPLE TESTING REGION -------------------------------------------->
# <-------------------------------------- STARTS SIMPLE TESTING REGION -------------------------------------------->

if __name__ == "__main__":
    SG = SupuestosGenerales()
    SG.agregar_categoria("ACTIVO","TEST")
    SG.agregar_categoria("SUSCRIPCIÓN","TEST2")

# <--------------------------------------  ENDS SIMPLE TESTING REGION  -------------------------------------------->
# <--------------------------------------  ENDS SIMPLE TESTING REGION  -------------------------------------------->
# <--------------------------------------  ENDS SIMPLE TESTING REGION  -------------------------------------------->