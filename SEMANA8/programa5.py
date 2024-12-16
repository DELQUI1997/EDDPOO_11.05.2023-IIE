# Implemente una clase llamada Celular que tenga como mínimo 5 atributos. Definir los siguientes métodos: para inicializar (__init__) y para mostrar datos. 
class Celular:
    #Atributos 
    def __init__(self):
        self.color = input("Ingrese el color:")
        self.modelo = input("Ingrese el modelo:")
        self.marca = input("Ingrese la marca:")
        self.camaras = int(input("Ingrese el numero de camaras:"))
        self.procesador = input("Tipo de procesador:")
    def mostrarDatos(self):
        print ("COLOR:", self.color)
        print ("MODELO:", self.modelo)
        print ("MARCA:", self.marca)
        print ("CAMARAS:", self.camaras)
        print ("PROCESADOR:", self.procesador)
        
# Creacion de objetos 
coche1 = Celular()
coche1.mostrarDatos()