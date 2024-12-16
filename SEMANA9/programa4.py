# Implementar una clase que represente una persona, que tenga como atributos codigo, nombre y edad. En el método __init__ cargar los atributos por teclado y luego ocultar cada uno de los atributos. Cree un objeto de la clase persona y usando print muestre el codigo, nombre y edad del objeto creado.

class Persona:
    
    def __init__(self):
        self.__codigo = input("Ingrese el codigo:")
        self.__nombre = input("Ingrese el nombre:")
        self.__edad = int(input("Ingrese la edad:"))
        # defiinicion de la clase de persona encapsulado
        
persona1 = Persona()
print("CODIGO:", persona1.__codigo)
print("CODIGO:", persona1.__nombre)
print("CODIGO:", persona1.__edad)


           