import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "SEMANA5/frmpagoEmpleado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class pagoEmpleado(QtWidgets.QMainWindow):

    def __init__(self):
        super(pagoEmpleado, self).__init__()
        uic.loadUi("SEMANA5/frmPagoEmpleado.ui", self)
        
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnSalir.clicked.connect(self.salir)
        self.show()
        
        #Datos de entrada 
    def procesar(self):
        horas = float(self.txtHoras.text())
        tarifa = float(self.txtTarifa.text())
        
        #Procesao de datos
        Subasico= horas * tarifa
        Subruto= Subasico+(Subasico*0.20)
        Suneto= Subruto-(Subruto*0.10)
        
        #Salida de datos
        self.txtS.setText("Sueldo Neto del Empleado:\n")
        self.txtS.append("Sueldo Basico\t:"+str(Subasico))
        self.txtS.append("Sueldo Bruto\t:"+str(Subruto))
        self.txtS.append("Sueldo Neto\t:"+str(Suneto))
        
    def salir(self):
        self.close()
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = pagoEmpleado()
    app.exec()
        
        
        