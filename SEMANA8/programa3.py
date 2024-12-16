class Auto:
    #Atributos 
    def __init__ (self, color, modelo, puertas, llantas, velocidades):
        self.color = color
        self.modelo = modelo
        self.puertas = puertas
        self.llantas = llantas
        self.velocidades = velocidades
    # metodos
    def mostrarDatos(self):
        print ("COLOR:", self.color)
        print ("MODELO:", self.modelo)
        print ("PUERTAs:", self.puertas)
        print ("LLANTAS:", self.llantas)
        print ("VELOCIDADES:", self.velocidades)
        
# Creacion de objetos 
coche1 = Auto("Rojo","Yaris", 4,4,5)
coche1.mostrarDatos()
