from input_manager import InputManager

class GeneralManager:

    def __init__(self):
        pass

    def validate_form(data = "", message = "", headers = [], nSpaceBetweenHeaders = 0):
        print(message+"\n")
        lastHeaderIndex = len(headers) - 1
        for index, element in enumerate(headers):
            if index != lastHeaderIndex:
                spaceBetweenHeaders = " " * (nSpaceBetweenHeaders - len(element))
            else: spaceBetweenHeaders = ""
            print(element + spaceBetweenHeaders,end='')
        try:
            blankIndex = [''] * len(data)
            data.index = blankIndex
        except:
            pass
        print("\n")
        print(data)
        print("")
        print("1) Si")
        print("2) No")
        selectedOption = InputManager.define_numbers(message="Ingresa la opción:", infLimit = 1, supLimit = 2,typeOfNumber = int)
        if selectedOption == 1: return True
        else: return False

        

        
