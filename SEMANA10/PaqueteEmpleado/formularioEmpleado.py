import sys
from PyQt5 import QtWidgets, uic
from claseEmpleado import Empleado  # es la clase que se encuentra aparte

qtCreatorFile = "SEMANA10/PaqueteEmpleado/frmEmpleado.ui"
Ui_MainWindow, QeBaseClass = uic.loadUiType(qtCreatorFile)

class FormularioEmpleado(QtWidgets.QMainWindow):
    def __init__(self):
        super(FormularioEmpleado, self).__init__()
        uic.loadUi("SEMANA10/PaqueteEmpleado/frmEmpleado.ui",self)
        
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show()
        
    def procesar(self):
        empleado1 = Empleado(1,"Delqui", 10, 10)
        self.mostrarDatos(empleado1)
        
    # -----------------------------------------------------------
    
    def imprimir(self, cad):
        self.txtS.append(cad)
        
    def mostrarDatos(self, Empleado):
        self.imprimir("Codigo\t:" + str(Empleado.getCodigo()))
        self.imprimir("Nombre\t:" + str(Empleado.getNombre()))
        self.imprimir("Horas\t:" + str(Empleado.getHoras()))
        self.imprimir("Tarifa\t:" + str(Empleado.getTarifa()))
        self.imprimir("sueldo bruto\t:" + str(Empleado.sueldoBruto()))
        self.imprimir("descuento\t:" + str(Empleado.descuento()))
        self.imprimir("sueldo neto\t:" + str(Empleado.sueldoNeto()))
        self.imprimir("")
    # -----------------------------------------------------------
    
    def limpiar(self):
        self.txtS.setText("")
    
    def salir(self):
        self.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windown = FormularioEmpleado()
    app.exec()



        
        