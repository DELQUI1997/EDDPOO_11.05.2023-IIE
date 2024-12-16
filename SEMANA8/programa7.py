# Implemente una clase llamada Operacion que tenga como atributos num1 y num2. Definir los siguientes métodos: para inicializar, para sumar, para restar, para multiplicar, para dividir y para mostrar resultado. 


class Operaciones:
    
    #Atributos
    def __init__(self):
        self.num1 = int(input("Ingrese primer numero:"))
        self.num2 = int(input("Ingrese segundo numero:"))
    
    def sumar(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        return self.num1 / self.num2
    
    # Metodos
    
    def mostrarDatos(self):
        print("LA SUMA ES:", self.sumar())
        print("LA RESTA ES:", self.resta())
        print("LA MULTIPLICACION ES:", self.multiplicar())
        print("LA DIVISION ES:", self.dividir())
        
# Creacion de Objetos
operacion1 = Operaciones()
operacion1.mostrarDatos()
    
    