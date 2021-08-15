from typing import Iterable


class InputManager:

    def __init__(self):
        pass

    def is_number(self, number, typeOfNumber = int):
        try:
            if typeOfNumber == int:
                number = int(number)
            elif typeOfNumber == float:
                number = float(number)
            return number
        except ValueError:
            return False

    def display_message(self, message):
        print(f"\n{message}")
        input("\nEnter para continuar\n")

    def define_numbers(self, message = "", messageKey="", infLimit = None, supLimit = None, quantity = 1,typeOfNumber= int):

        numbers = []
        iter = 0
        while iter < quantity:
            if messageKey != "":
                displayMessage = message + f" [{messageKey} {iter}]: "
            else:
                displayMessage = message+" "
            number = isNumber = self.is_number(input(displayMessage), typeOfNumber)

            if isNumber is not False: 
                if infLimit is not None and number < infLimit:
                    self.display_message(f"Error, el valor {number} debe ser superior a {infLimit}")
                    iter -= 1
                elif supLimit is not None and number > supLimit:
                    self.display_message(f"Error, el valor {number} debe ser inferior a {supLimit}")
                else:
                    numbers.append(number)
            else:
                self.display_message(f"Error, el valor {number} no es un elemento aceptado")
                iter -= 1

            iter += 1
        
        if len(numbers) != 1:
            return numbers
        else:
            return numbers[0]
    
    def define_string(self, message ="", infLimit = None, supLimit = None):
        while True:
            string = input(message+" ")
            if infLimit is not None and len(string) < infLimit:
                self.display_message(f"Error, la longitud de '{string}' debe ser superior a {infLimit}")
            elif supLimit is not None and len(string) > supLimit:
                self.display_message(f"Error, la longitud de '{string}' debe ser inferior a {supLimit}")
            else:
                return string

            



    


#SIMPLE TESTING ENVIRONMENT
if __name__ == "__main__":
    IM = InputManager()

    numeros = IM.define_numbers(message="Ingresa tu número", messageKey="Número",quantity=5, typeOfNumber=float)
    if isinstance(numeros,Iterable):
        for numero in numeros:
            print(f"Numero: {numero}")
    else:
        print(f"Numero: {numeros}")



            



