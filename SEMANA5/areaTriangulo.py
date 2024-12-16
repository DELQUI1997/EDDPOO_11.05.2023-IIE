import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "SEMANA5/frmAreaTriangulo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class FormularioAreaTriangulo(QtWidgets.QMainWindow):

    def __init__(self):
        super(FormularioAreaTriangulo, self).__init__()
        uic.loadUi("SEMANA5/frmAreaTriangulo.ui", self)
        
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnLimpar.clicked.connect(self.limpar)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show()
        
    def calcular(self):
        # Entrada de datos
        base=float(self.txtBase.text())
        altura=float(self.txtAltura.text())
        
        # Proceso de calculo
        area=(base*altura )/2
        
        # Salida de resultados
        self.txtS.setText("AREA DE TRIANGULO:\n")
        self.txtS.append("El valor de la base es\t:" + str(base))
        self.txtS.append("El valor de la altura es\t:" + str(altura))
        self.txtS.append("El valor de la area es\t:" + str(area))
    
    
    def limpar(self):
        self.txtBase.setText("")
        self.txtAltura.setText("")
        self.txtS.setText("")
        
    def salir(self):
        self.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioAreaTriangulo()
    app.exec()
