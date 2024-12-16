# Implemente una clase llamada Casa que tenga como mínimo 5 atributos. Definir los siguientes métodos: para inicializar (__init__) y para mostrar datos. 

class Hogar:
    #Atributos 
    def __init__(self):
        self.pisos = int(input("Numero de pisoso:"))
        self.color = input("Color de la casa:")
        self.cuartos = int(input("Numero de cuartos:"))
        self.labatorio = int(input("Cantidad de labatorios:"))
        self.salas = int(input("Cantidad de salas:"))
    def mostrarDatos(self):
        print ("PISOS:", self.pisos)
        print ("COLOR:", self.color)
        print ("CUARTOS:", self.cuartos)
        print ("LABATORIO:", self.labatorio)
        print ("SALAS:", self.salas)
        
# Creacion de objetos 
casa1 = Hogar()
casa1.mostrarDatos()