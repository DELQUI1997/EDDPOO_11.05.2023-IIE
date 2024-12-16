# Implementar una clase que represente una persona, que tenga como atributos codigo, nombre y edad. En el método __init__ cargar los atributos por teclado y luego ocultar cada uno de los atributos. Crear los métodos get y set para acceder y modificar los atributos fuera de la clase. Cree un objeto de la clase persona y usando print muestre el codigo, nombre y edad del objeto creado.

# get ----> permite acceder al atributo oculto
# set -----> asignar

class Persona:
    
    # metodo contructor
    
    def __init__(self):
        
        self.__codigo =input("Ingrese el codigo:")
        self.__nombre =input("Ingrese el nombre:")
        self.__edad =input("Ingrese la edad:")
     #-----------------------------------------------------------------------------------   
    # metodo de acceso get y set
    
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre      # con estos codigos se acceso a los atributos ocultos
    
    def getEdad(self):
        return self.__edad
     #-----------------------------------------------------------------------------------
     # metod de asignacion
    def setCodigo(self, codigo):
        self.__codigo = codigo
        
    def setNombre(self, nombre):   # con estos codigos asignamos a los atributos 
        self.__nombre = nombre
        
    def setEdad(self, edad):
        self.__edad = edad
    #-----------------------------------------------------------------------------------
    
persona1 = Persona()
print("CODIGO:", persona1.getCodigo())
print("NOMBRE:", persona1.getNombre())
print("EDAD:", persona1.getEdad())
