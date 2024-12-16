from PyQt5 import QtWidgets, uic
from Vista.VentanaPrincipal import VentanaPrincipal
qtCreatorFile = "Proyecto/UI/Login.ui"
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class login(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        super(login, self).__init__(parent)
        uic.loadUi("Proyecto/UI/Login.ui", self)
        self.btnIniciar.clicked.connect(self.iniciarsesion)
        
        self.show()
        
    def iniciarsesion(self):
        usuario = self.txtUsuario.text()
        contraseña = self.txtPassword.text()
        if usuario == "Delqui" and contraseña == "123456":
            self.close()
            vprincipal = VentanaPrincipal(self)
            vprincipal.show()
        
