class Alumno:
    def __init__(self, codigo, nombres, apellidos, ciclo, pension, carrera, sede):
        self.__codigo = codigo
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__ciclo = ciclo
        self.__pension = pension
        self.__carrera = carrera
        self.__sede = sede
        
    def getCodigo(self):
        return self.__codigo
    
    def getNombres(self):
        return self.__nombres
    
    def getApellidos(self):
        return self.__apellidos
    
    def getCiclo(self):
        return self.__ciclo
    
    def getPension(self):
        return self.__pension
    
    def getCarrera(self):
        return self.__carrera
    
    def getSede(self):
        return self.__sede
    
    
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
        
    def setNombres(self, nombres):
        self.__nombres = nombres
        
    def setApellidos(self, apellidos):
        self.__apellidos = apellidos
        
    def setCiclo(self, ciclo):
        self.__ciclo = ciclo
        
    def setPension(self, pension):
        self.__pension = pension
        
    def setCarrera(self, carrera):
        self.__carrera = carrera
        
    def setCarrera(self, sede):
        self.__sede = sede