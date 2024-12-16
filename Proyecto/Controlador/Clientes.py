class Cliente:
    def __init__(self, dni, nombre, apellidoPaterno, apellidoMaterno, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidoPaterno = apellidoPaterno
        self.__apellidoMaterno = apellidoMaterno
        self.__direccion = direccion 
        self.__telefono = telefono
        
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellidoPaterno(self):
        return self.__apellidoPaterno
    
    def getApellidoMaterno(self):
        return self.__apellidoMaterno
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    
    
    def setDni(self, dni):
        self.__dni = dni
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setApellidoPaterno(self, apellidoPaterno):
        self.__apellidoPaterno = apellidoPaterno
        
    def setApellidoMaterno(self, apellidoMaterno):
        self.__pellidoMaterno = apellidoMaterno
        
    def setDireccion(self, direccion):
        self.__direccion = direccion 
        
    def setTelefono(self, telefono):
        self.__telefono = telefono
    
        
    