class Alumno:
    
    # Constructor
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        
    # Metodos 
    def promedio(self):
        return (self.nota1 + self.nota2) /2
    
    