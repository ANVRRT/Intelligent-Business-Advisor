from input_manager import InputManager
from os_manager import OSManager
import pandas as pd
import numpy as np


class SupuestosGenerales:

    def __init__(self):
        pass

    def safe_file(self,fileName, file,data):
        if fileName == "categorias.csv":
            
            if (OSManager().get_file_size(fileName) == 0):
                initialRegistry = "CATEGORIA" + "," + "J1" + "," + "J2" + "\n"
                file.write(initialRegistry)
                file.close()
            # ----------------------
            pandasFile = OSManager().open_pandas_csv_file(file.name)
            # ----------------------
            if (len(pandasFile.index) >= 10):
                return "CAT_LIMIT"

            # print(len(pandasFile.index))

            # ----------------------
            pandasFile.set_index(["CATEGORIA"], inplace = True)
            # ----------------------

            registry = pd.DataFrame({
                                    "J1": [data[0]],
                                    "J2": [data[1]]
                                    })
            indexLabel = "CATEGORIA"
            # print(pandasFile)

        pandasFile = pandasFile.append(registry)
        pandasFile.reset_index(drop = True, inplace = True)
        pandasFile.index = pandasFile.index + 1
        pandasFile.to_csv(file.name, index_label = indexLabel)

            # print(pandasFile)

                
            

    def add_category(self, J1, J2):
        
        # file = open("./SupuestosGenerales/Generales/Categorias/categorias.csv","a")
        fileName = "categorias.csv"
        data = [J1,J2]
        file = OSManager().create_file(f"./SupuestosGenerales/Generales/Categorias/{fileName}", output = True)

        # file = OSManager().open_pandas_csv_file(f"./SupuestosGenerales/Generales/Categorias/{fileName}")
        errorMessage = self.safe_file(fileName,file,data)
        file.close()
        return errorMessage


# <-------------------------------------- STARTS SIMPLE TESTING REGION -------------------------------------------->
# <-------------------------------------- STARTS SIMPLE TESTING REGION -------------------------------------------->
# <-------------------------------------- STARTS SIMPLE TESTING REGION -------------------------------------------->

if __name__ == "__main__":
    SG = SupuestosGenerales()
    print(SG.add_category("ACTIVO","TEST"))
    print(SG.add_category("PPV","TEST"))
    print(SG.add_category("PUBLICIDAD","TEST"))


# <--------------------------------------  ENDS SIMPLE TESTING REGION  -------------------------------------------->
# <--------------------------------------  ENDS SIMPLE TESTING REGION  -------------------------------------------->
# <--------------------------------------  ENDS SIMPLE TESTING REGION  -------------------------------------------->