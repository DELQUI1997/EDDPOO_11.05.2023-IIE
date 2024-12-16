import sys
from PyQt5 import QtWidgets, uic
from claseEmpleado import Empleado  # es la clase que se encuentra aparte

qtCreatorFile = "EC3_FARCEQUE_MINGA/PaqueteEmpleado/frmEmpleado.ui"
Ui_MainWindow, QeBaseClass = uic.loadUiType(qtCreatorFile)

class FormularioEmpleado(QtWidgets.QMainWindow):
    def __init__(self):
        super(FormularioEmpleado, self).__init__()
        uic.loadUi("EC3_FARCEQUE_MINGA/PaqueteEmpleado/frmEmpleado.ui",self)
        
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show()
        
    def procesar(self):
        empleado1 = Empleado("B1710076","DELQUI FARCEQUE MINGA", "70998443",  20, 15)
        self.mostrarDatos(empleado1)
        
    # -----------------------------------------------------------
    
    def imprimir(self, cad):
        self.txtS.append(cad)
        
    def mostrarDatos(self, Empleado):
        self.imprimir("CODIGO\t\t:" + str(Empleado.getCodigo()))
        self.imprimir("NOMBRE\t\t:" + str(Empleado.getNombre()))
        self.imprimir("DNI\t\t:" + str(Empleado.getDni()))
        self.imprimir("HORAS\t\t:" + str(Empleado.getHoras()))
        self.imprimir("TARIFA\t\t:" + str(Empleado.getTarifa()))
        self.imprimir("SUELDO BRUTO\t\t:" + str(Empleado.sueldoBruto()))
        self.imprimir("DESCUENTO ESSALUD (12%)\t:" + str(Empleado.descuento1()))
        self.imprimir("DESCUENTO AFP (11%)\t:" + str(Empleado.descuento2()))
        self.imprimir("DESCUENTO TOTAL\t:" + str(Empleado.totalDescuento()))
        self.imprimir("SUELDO NETO\t\t:" + str(Empleado.sueldoNeto()))
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



        
         