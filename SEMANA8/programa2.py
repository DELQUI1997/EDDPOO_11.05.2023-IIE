'''
sintaxis 
 
def <nombre metodo> (self):

    <acciones>
    
'''

class Auto:
    #Atributos 
    def inicializar(self):
        self.color = input("Ingrese el color:")
        self.modelo = input("Ingrese el modelo:")
        self.puertas = int(input("Ingrese las puertas:"))
        self.llantas = int(input("Ingrese las llantas:"))
        self.velocidades = int(input("Ingrese las velocidades:"))
    def mostrarDatos(self):
        print ("COLOR:", self.color)
        print ("MODELO:", self.modelo)
        print ("PUERTAs:", self.puertas)
        print ("LLANTAS:", self.llantas)
        print ("VELOCIDADES:", self.velocidades)
        
# Creacion de objetos 
coche1 = Auto()
coche1.inicializar()
coche1.mostrarDatos()

# init = sirbe para reen=mplazar al igual que inicializar
