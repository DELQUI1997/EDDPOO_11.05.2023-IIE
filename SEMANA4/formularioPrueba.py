import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "SEMANA4/frmPrueba.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class FormularioPrueba(QtWidgets.QMainWindow):

    def __init__(self):
        super(FormularioPrueba, self).__init__()
        uic.loadUi("SEMANA4/frmPrueba.ui", self)
        
        
        
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show()    
    def procesar(self):
        self.lblTexto.setText("Mi Nombre es Delqui...!!")   # hacer llamado del texto

    def limpiar(self):
        self.lblTexto.setText("Pulsa nuevamente en el botón Procesar...!!!")
    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioPrueba()
    app.exec()
