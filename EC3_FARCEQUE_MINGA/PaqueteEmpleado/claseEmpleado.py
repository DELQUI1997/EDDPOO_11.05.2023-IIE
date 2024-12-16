class Empleado:
    
    # Constructor
    def __init__(self, codigo, nombre, dni, horas, tarifa):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__dni = dni
        self.__nombre = nombre
        self.__horas = horas
        self.__tarifa = tarifa
    # Metodos de  acceso get y set
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def getHoras(self):
        return self.__horas
    
    def getTarifa(self):
        return self.__tarifa
    
    # metodos  acceso a set
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setNombre(self, dni):
        self.__dni = dni
        
     
    def setHoras(self, horas):
        self.__horas = horas
        
    def setTarifa(self, tarifa):
        self.__tarifa = tarifa
        
    # Metodos de calculo
    
    def sueldoBruto(self):
        return self.getHoras() * self.getTarifa ()
    
    def descuento1(self):
        return 0.12 * self.sueldoBruto()
    
    def descuento2(self):
        return 0.11 * self.sueldoBruto()
    
    def totalDescuento(self):
        return self.descuento1 ()  + self.descuento2()
    
    def sueldoNeto(self):
        return self.sueldoBruto()  - self.totalDescuento()
    
    
    
    
        
 
        

   
    