from input_manager import InputManager
from os_manager import OSManager
import pandas as pd
import numpy as np


class SupuestosGenerales:

    def __init__(self):
        pass

    def write_file_header(self,fileName):                                                                           #Writes file header in case is empty

        if (OSManager.get_file_size(fileName) == 0):
            if fileName == "categorias.csv":
                file = OSManager.create_file(f"./SupuestosGenerales/Generales/Categorias/{fileName}", output = True) #Opens and returns opened file
                initialRegistry = "CATEGORIA" + "," + "J1" + "," + "J2" + "\n"                                       #Defines header 
        
            file.write(initialRegistry)                                                                              #Writes header
            file.close()                                                                                                 #Closes file


    def save_file(self,fileName, filePath, data, editMode = False, categoryNumber = 0):                              #Saves the sent data in the indicated file
        pandasFile = OSManager.open_pandas_csv_file(filePath)                                                        #Opens the indicated file into a pandas dataframe

        if fileName == "categorias.csv":
            indexLabel = "CATEGORIA"
            pandasFile.set_index([indexLabel], inplace = True)                                                       #Defines first column named 'CATEGORIA' into index

            if editMode:                                                                                             
                pandasFile.at[categoryNumber,["J1","J2"]] = data                                                     #If is in edit mode, indicated row
            else:
                if (len(pandasFile.index) >= 10):                                                                    #If maximum number of categories allowed is reached, return error
                    return "CAT_LIMIT"

                registry = pd.DataFrame({                                                                            #Prepares registry of new category
                                        "J1": [data[0]],
                                        "J2": [data[1]]
                                        })
                
                # print(pandasFile)
                pandasFile = pandasFile.append(registry)                                                             #Adds new category into pandas dataframe

        
        pandasFile.reset_index(drop = True, inplace = True)                                                          #Resets index from 1 to 10
        pandasFile.index = pandasFile.index + 1                                                                      #Increases index +1, to start in 1 and not in 0
        pandasFile.to_csv(filePath, index_label = indexLabel)                                                        #Writes pandas dataframe into csv file

            # print(pandasFile)

                
            

    def add_category(self, J1, J2):                                                                                  #Adds new category
        
        fileName = "categorias.csv"                                                                                  #Defines fileName into 'categorias.csv'
        filePath = "./SupuestosGenerales/Generales/Categorias/categorias.csv"                                        #Defines 'categorias.csv' file path
        self.write_file_header(fileName)                                                                             #If the file is empty, writes the header

        data = [J1,J2]                                                                                               #Groups data into an array (list)

        errorMessage = self.save_file(fileName,filePath,data)                                                        #Saves data into the indicated file

        return errorMessage                                                                                          #If there's an error, returns the error, if not returns None

    def edit_category(self, categoryNumber, J1, J2):                                                                 #Edits category

        fileName = "categorias.csv"                                                                                  #Defines fileName into 'categorias.csv'
        filePath = "./SupuestosGenerales/Generales/Categorias/categorias.csv"                                        #Defines 'categorias.csv' file path
        
        data = [J1, J2]                                                                                              #Groups data into an array (list)

        errorMessage = self.save_file(fileName,filePath,data, editMode = True, categoryNumber = categoryNumber)      #Saves the indicated category with the new data

        return errorMessage                                                                                          #If there's an error, returns the error, if not returns None


# <-------------------------------------- STARTS SIMPLE TESTING REGION -------------------------------------------->
# <-------------------------------------- STARTS SIMPLE TESTING REGION -------------------------------------------->
# <-------------------------------------- STARTS SIMPLE TESTING REGION -------------------------------------------->

if __name__ == "__main__":
    SG = SupuestosGenerales()
    print(SG.add_category("ACTIVO","TEST"))
    print(SG.add_category("PPV","TEST"))
    print(SG.add_category("PUBLICIDAD","TEST"))
    SG.edit_category(1,"PUBLICICAD","EDIT3")
    


# <--------------------------------------  ENDS SIMPLE TESTING REGION  -------------------------------------------->
# <--------------------------------------  ENDS SIMPLE TESTING REGION  -------------------------------------------->
# <--------------------------------------  ENDS SIMPLE TESTING REGION  -------------------------------------------->