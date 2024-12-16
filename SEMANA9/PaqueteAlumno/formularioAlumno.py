import sys
from PyQt5 import QtWidgets, uic
from claseAlumno import Alumno   # es la clase que se encuentra aparte

qtCreatorFile = "SEMANA9/PaqueteAlumno/frmAlumno.ui"
Ui_MainWindow, QeBaseClass = uic.loadUiType(qtCreatorFile)

class FormularioAlumno(QtWidgets.QMainWindow):
    def __init__(self):
        super(FormularioAlumno, self).__init__()
        uic.loadUi("SEMANA9/PaqueteAlumno/frmAlumno.ui",self)
        
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show()
        
    def procesar(self):
        alumno1 = Alumno("Delqui", 18, 15)
        self.mostrarDatos(alumno1)
        
        alumno2 = Alumno("Leoncio", 18, 19)
        self.mostrarDatos(alumno2)
        
        alumno3 = Alumno("Margarita", 18, 15)
        self.mostrarDatos(alumno3)
    
    # -----------------------------------------------------------
    
    def imprimir(self, cad):
        self.txtS.append(cad)
        
    def mostrarDatos(self, Alumno):
        self.imprimir("Nombre\t:" + str(Alumno.nombre))
        self.imprimir("Nota1\t:" + str(Alumno.nota1))
        self.imprimir("Nota2\t:" + str(Alumno.nota2))
        self.imprimir("Promedio\t:" + str(Alumno.promedio()))
        self.imprimir("")
    # -----------------------------------------------------------
    
    def limpiar(self):
        self.txtS.setText("")
    
    def salir(self):
        self.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windown = FormularioAlumno()
    app.exec()



        
        