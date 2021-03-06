from utils import *

class MainMenu:
    def menu_ximulator(self):
        print("")
        print("*****************************************************")
        print("BIENVENIDO A XIMULATOR")
        print("")
        print("1) Supuestos generales")             #CODING
        print("2) Inversión y Financiamiento")      #NOT CODED
        print("3) Proyección financiera")           #NOT CODED
        print("4) Salir")
        print("")
        print("*****************************************************")
        # op=pf.pide_numero("Ingresa el número correspondiente a las opciones mostradas: ", 1,4,"int")
        selectedOption = InputManager.define_numbers(message="Ingresa el número correspondiente a las opciones mostradas:", infLimit = 1, supLimit = 4,typeOfNumber = int)
        print("")
        return (selectedOption)

class MenuSupuestosGenerales:


    def main_menu(self):
        selectedOption=0
        while selectedOption!=4:
            OSManager.clear_console_log()
            print("")
            print("*****************************************************")
            print("MENÚ SUPUESTOS GENERALES")
            print("")
            print("1) Generales")           #CODING
            print("2) Costos y gastos")     #NOT CODED
            print("3) Ingresos")            #NOT CODED
            print("4) Regresar")
            print("")
            print("*****************************************************")
            # op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,4,"int")
            selectedOption = InputManager.define_numbers(message="Ingresa el número correspondientes a tu selección:", infLimit = 1, supLimit = 4,typeOfNumber = int)

            print("")
            OSManager.clear_console_log()
            if selectedOption==1:
                
                self.menu_generales()
                pass
            if selectedOption == 2:
                # costos_gastos()
                pass
            if selectedOption == 3:
                # ingresos()
                pass
    

    def menu_generales(self):
        selectedOption=0
        while selectedOption!=5:
            OSManager.clear_console_log()
            print("")
            print("*****************************************************")
            print("MENÚ GENERALES")
            print("")
            print("1) Categorías")                      #CODED              #MISSING DELETE CATEGORY
            print("2) Inflación de costos y gastos")    #NOT CODED
            print("3) Incremento de ventas")            #NOT CODED
            print("4) Impuestos/Dividendos/TC")         #NOT CODED
            print("5) Regresar")
            print("")
            print("*****************************************************")
            # op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
            selectedOption = InputManager.define_numbers(message="Ingresa el número correspondientes a tu selección:", infLimit = 1, supLimit = 5,typeOfNumber = int)
            OSManager.clear_console_log()

            if selectedOption == 1:                                                                                 #CATEGORY MENU OPTION
                selectedOption = self.menu_categorias()
                
                if selectedOption == 2:
                    InputManager.display_message("Enter para continuar a inflación de costos y gastos")
                
            if selectedOption == 2:
                selectedOption = inflacion()
                if selectedOption == 3:
                    InputManager.display_message("Enter para continuar a incremento de ventas")
                
            if selectedOption == 3:
                selectedOption = incremento_ventas()
                if selectedOption == 4:
                    InputManager.display_message("Enter para continuar a impuestos/Dividendos/TC")
                
            if selectedOption == 4:
                impuestos()
                print("Usted ha terminado la sección de 'Generales' ")
                InputManager.display_message("Enter para continuar")

    def menu_categorias(self):
        # <-------------------------------------- STARTS CREATE CATEGORY REGION -------------------------------------------->
        # <-------------------------------------- STARTS CREATE CATEGORY REGION -------------------------------------------->
        # <-------------------------------------- STARTS CREATE CATEGORY REGION -------------------------------------------->
        
        def agregar(editMode = False):
            selectedOption = 0
            SPACE_BETWEEN_HEADERS = 12
            while selectedOption != 5:
                OSManager.clear_console_log()
                print("")
                print("*****************************************************")
                print("MENÚ DEFINICIÓN DE CATEGORÍA")
                print("")
                print("1) Activo")
                print("2) Suscripción")
                print("3) Publicidad")
                print("4) PPV")
                print("5) Salir")   
                print("")
                print("*****************************************************")
                selectedOption = InputManager.define_numbers(message="Ingresa el número correspondientes a tu selección:", infLimit = 1, supLimit = 5,typeOfNumber = int)
                if selectedOption == 1:
                    J1 = "ACTIVO"
                if selectedOption == 2:
                    J1 = "SUSCRIPCION"
                if selectedOption == 3:
                    J1 = "PUBLICIDAD"
                if selectedOption == 4:
                    J1 = "PPV"
                if selectedOption == 5:
                    break
                # pf.pide_cadena("Ingresa el nombre de tu categoría :",1,15)
                J2 = InputManager.define_string(message = "Ingresa el nombre de tu categoría:", infLimit = 1, supLimit = 15).upper()
                registry = J1 + (" " * (SPACE_BETWEEN_HEADERS - len(J1))) + J2
                validation = GeneralManager.validate_form(data = registry, message = "Ingresa la opción:", headers = ["Tipo","Nombre"], nSpaceBetweenHeaders = SPACE_BETWEEN_HEADERS)

                if validation == True: #CREATES NEW CATEGORY
                    if editMode: return (J1,J2)
                    errorMessage = SupuestosGenerales.add_category(J1,J2)
                    if (errorMessage == "CAT_LIMIT"): 
                        InputManager.display_message("Has excedido el límite de categorías, edita o elimina una para continuar")
                    else:
                        InputManager.display_message("Tu categoría ha sido exitosamente guardada")


                if validation == False: InputManager.display_message("Tu categoría ha sido exitosamente eliminada, ingresala nuevamente")

        # <--------------------------------------  ENDS CREATE CATEGORY REGION  -------------------------------------------->
        # <--------------------------------------  ENDS CREATE CATEGORY REGION  -------------------------------------------->
        # <--------------------------------------  ENDS CREATE CATEGORY REGION  -------------------------------------------->

        # <-------------------------------------- STARTS SHOW REPORT REGION -------------------------------------------->
        # <-------------------------------------- STARTS SHOW REPORT REGION -------------------------------------------->
        # <-------------------------------------- STARTS SHOW REPORT REGION -------------------------------------------->
        def reporte():
            # report = pd.read_csv()
            report = OSManager.open_pandas_csv_file("./SupuestosGenerales/Generales/Categorias/categorias.csv")
            GeneralManager.print_report(report)

        # <--------------------------------------  ENDS SHOW REPORT REGION  -------------------------------------------->
        # <--------------------------------------  ENDS SHOW REPORT REGION  -------------------------------------------->
        # <--------------------------------------  ENDS SHOW REPORT REGION  -------------------------------------------->


        # <-------------------------------------- STARTS EDIT CATEGORY REGION -------------------------------------------->
        # <-------------------------------------- STARTS EDIT CATEGORY REGION -------------------------------------------->
        # <-------------------------------------- STARTS EDIT CATEGORY REGION -------------------------------------------->
        def editar_categoria():
            categoryNumber = InputManager.define_numbers(message="Ingresa el número correspondientes a tu selección:", infLimit = 1, supLimit=10,typeOfNumber = int)

            try:
                J1, J2 = agregar(editMode = True)
                errorMessage = SupuestosGenerales.edit_category(categoryNumber, J1, J2)
            except:
                return
            

        # <--------------------------------------  ENDS EDIT CATEGORY REGION  -------------------------------------------->
        # <--------------------------------------  ENDS EDIT CATEGORY REGION  -------------------------------------------->
        # <--------------------------------------  ENDS EDIT CATEGORY REGION  -------------------------------------------->

        selectedOption=0
        cont_cat=0
        while selectedOption!=5:
            OSManager.clear_console_log()
            print("")
            print("*****************************************************")
            print("MENÚ CATEGORÍAS")
            print("")
            print("1) Agregar")             #CODED
            print("2) Reporte")             #CODED
            print("3) Editar categoría")    #CODED
            print("4) Siguiente")           #CODED
            print("5) Atrás")
            print("")
            print("*****************************************************")
            selectedOption = InputManager.define_numbers(message="Ingresa el número correspondientes a tu selección:", infLimit = 1, supLimit=5,typeOfNumber = int)

            OSManager.clear_console_log()
            if selectedOption == 1: # Add category
                agregar()
                
            if selectedOption == 2: # Print report
                reporte()
                InputManager.display_message("")

            if selectedOption == 3:
                reporte()
                print("")
                editar_categoria()
            
            if selectedOption == 4:
                return 2
            




if __name__ == "__main__":

    # Console Menu Initializator
    #Initialize objects
    Menu = MainMenu()                          #Initialize MainMenu class object
    # InputManager = InputManager()              #Initialize InputManager class object
    # GeneralManager = GeneralManager()          #Initialize GeneralManager class object     
    # OSManager = OSManager()                    #Initialize OSManager class object


    OSManager.clear_console_log()
    selectedOption = 0
    while selectedOption!=4:
        selectedOption = Menu.menu_ximulator()
        OSManager.clear_console_log()
        if selectedOption == 1: #Supuestos Generales
            SupuestosGenerales = SupuestosGenerales()           #Initialize SupuestosGenerales class object

            #Open Supuestos Generales Menu
            MenuSupuestosGenerales = MenuSupuestosGenerales()   #Initialize MenuSupuestosGenerales class object
            MenuSupuestosGenerales.main_menu()

            # InputManager.display_message("TESTING")
        


