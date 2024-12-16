from PyQt5 import QtWidgets, uic

class VentanaAlumnos(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaAlumnos, self).__init__(parent)
        uic.loadUi("UI/frmAlumnos.ui", self)
    
        self.show()