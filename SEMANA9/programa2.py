# Implemente la clase Animal, que tenga como atributos nombre, numero_patas y tamaño. En el método __init__ cargar los atributos por teclado y en otro método mostrar sus datos. Luego  implemente la clase Canino que tiene como atributo raza y la clase Perro que tiene como atributo numero_vacunas, la clase Canino hereda de la clase Animal y la clase Perro hereda de la clase Canino. Finalmente cree dos objetos de la clase Perro.

class Animal:
     
    def __init__(self):
    
        self.nombre = input ("Ingrese el nombre del animal:")
        self.numero_patas = input ("Ingrese el numero de patas:")
        self.tamaño = input ("Ingrese el tamaño del animal:")
        
    def mostrarDatos(self):
        print("Nombre", self.nombre)
        print("Numero de patas:", self.numero_patas)
        print("Tamaño:", self.tamaño)
        
class Canino(Animal):
    
    def __init__(self):
        super(). __init__()  # super atrae a los atributos
        self.raza = input("ingrese la raza:")
        
    def mostrarDatos(self):
        super().mostrarDatos()
        print("Raza:", self.raza)
        
        
    