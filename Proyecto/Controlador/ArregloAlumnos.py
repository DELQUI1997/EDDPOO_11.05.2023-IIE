from Controlador.Alumnos import Alumno

class ArregloAlumnos:
    
    def __init__(self):
        self.dataAlumnos = []
        self.cargar()
     
    def cargar(self):
        archivo = open("Proyecto/Modelo/Alumnos.txt", "r")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna [0]
            nombres = columna [1]
            apellidos = columna [2]
            ciclo = columna [3]
            pension = columna [4]
            carrera = columna [5]
            sede = columna [6].strip()
            objAlu = Alumno(codigo, nombres, apellidos, ciclo, pension, carrera, sede)
            self.adicionaAlumno(objAlu)
        archivo.close()
        
        
    def grabar(self):
        archivo = open ("Proyecto/Modelo/Alumnos.txt", "w")
        for i in range (self.tamanoArregloAlumno()):
            archivo.write(str(self.devolverAlumno(i).getCodigo()) + ","
                          + str(self.devolverAlumno(i).getNombres()) + ","
                          + str(self.devolverAlumno(i).getApellidos()) + ","
                          + str(self.devolverAlumno(i).getCiclo()) + ","
                          + str(self.devolverAlumno(i).getPension()) + ","
                          + str(self.devolverAlumno(i).getCarrera()) + ","
                          + str(self.devolverAlumno(i).getSede()) + "\n")
        archivo.close()
                          
                          
                        
        
            
    
            
    def adicionaAlumno(self, objAlu):
        self.dataAlumnos.append(objAlu)
        
    def devolverAlumno(self, pos):
        return self.dataAlumnos[pos]
    
    def tamanoArregloAlumno(self):
        return len(self.dataAlumnos)
    
    def buscarAlumno(self, codigo):
        for i in range(self.tamanoArregloAlumno()):
            if codigo == self.dataAlumnos[i].getCodigo():
                return i
        return -1
    
    def eliminarAlumno(self, indice):
        del(self.dataAlumnos[indice])