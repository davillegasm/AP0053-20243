from Suma import Suma
from Resta import Resta
from Multiplicacion import Multiplicacion
from Division import Division
from Operando import Operando 

class Menu:
    def __init__(self):
        self.opcion = None
        self.op1 = 0
        self.op2 = 0

    def mostrar_menu(self):
        while True:
            print("buenas, vamos a calcular, elije una opcion")
            print("1) Suma")
            print("2) Resta")
            print("3) Multiplicacion")
            print("4) Division")
            print("5) Salir")
            self.opcion = input("elije una operacion ")
            if self.opcion in ["1", "2", "3", "4"]:
                 while True:
                    try:
                        self.op1 = float(input("Ingrese 1 numero "))
                        self.op2 = float(input("Ingrese otro numero "))
                        break 
                    except ValueError:
                        print("ingrese numeros validos")           
            operando = Operando(self)  
            operando.realizar_operacion()  
            if   self.opcion == "5":
                print("hasta luego")
                break     
           
             