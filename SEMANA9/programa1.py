# Implemente la clase Animal, que tenga como atributos nombre, numero_patas y tamaño. En el método __init__ cargar los atributos por teclado y en otro método mostrar sus datos. Luego  implemente la clase Perro y la clase Gato que hereden de la clase Animal. Finalmente cree un objeto de las clases hijas uno para cada clase.

# Defiinicion de la clase animal
class Animal:
    def __init__(self):
        
        self.nombre = input ("Ingrese el nombre del animal:")
        self.numero_patas = input ("Ingrese el numero de patas:")
        self.tamaño = input ("Ingrese el tamaño del animal:")
        
    def mostrarDatos(self):
        
        print("Nombre", self.nombre)
        print("Numero de patas:", self.numero_patas)
        print("Tamaño:", self.tamaño)
 # ------------------------------------------------------------------------       
class Perro(Animal):
    pass

class Gato(Animal):
    pass

perro1 = Perro()
perro1.mostrarDatos()

gato1 = Gato()
gato1.mostrarDatos()
        


        