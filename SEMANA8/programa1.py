'''
sintaxis 
 
def <nombre metodo> (self):

    <acciones>
    
'''

class Auto:
    #Atributos 
    def inicializar(self, color, modelo, puertas, llantas, velocidades):
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
coche1 = Auto()
coche1.inicializar("Rojo","Yaris",4,4,5)
coche1.mostrarDatos()
print ("==========================================")
coche2 = Auto()
coche2.inicializar("Verde","Yaris",4,4,5)
coche2.mostrarDatos()
print ("==========================================")
coche3 = Auto()
coche3.inicializar("Negro","Yaris",4,4,5)
coche3.mostrarDatos()
print ("==========================================")
