print("Bienvenido al calculador basico de numeros")

valor_a = int(input("ingrese el valor_a, con el que desea operar "))
valor_b = int(input("ingrese el valor_b, con el que desea operar "))
valor_c = 0
valor_d = 0

class calculador:
    
    def __init__(self,suma,resta,multiplicacion,division):
        self.suma = suma
        self.resta = resta
        self.multiplicacion = multiplicacion
        self.division = division
        
    def sumar(self):
        print("la suma de ambos valores son ", valor_a + valor_b)
        
    def restar(self):
        print("la resta de ambos valores son ", valor_a - valor_b)
        
    def multiplicar(self):
        print("la multiplicacion de ambos valores son ", valor_a * valor_b)
        
    def dividir(self):
        print("la division de ambos valores son ", valor_a / valor_b)
        
calc = calculador(valor_a, valor_b, valor_c, valor_d)
calc.sumar()
calc.restar()
calc.multiplicar()
calc.dividir()

valor_a = int(input("Gracias por usar el programa :) "))