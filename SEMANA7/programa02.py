class Auto:     #una clase siempre va ha tener atributos y metodos
    # Atributos 
    color = ""
    modelo = ""
    puertas = ""
    llantas = 0
    velocidades = 0
    
    # Metodos 
    def mostrarDatos(self): # self para referenciar ya sea tributo o metodo
        print ("COLOR:", self.color)
        print ("MODELO:", self.modelo)
        print ("PUERTAs:", self.puertas)
        print ("LLANTAS:", self.llantas)
        print ("VELOCIDADES:", self.velocidades)
        
        
# Instancia de clase de Auto
coche1 = Auto()
coche1.color = "Azul"
coche1.modelo = "Yaris"
coche1.puertas = 4
coche1.llantas = 4
coche1.velocidades = 5

coche1.mostrarDatos()
