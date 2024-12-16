import sys
from PyQt5 import QtWidgets, uic
qtCreatorFile = "EC2_FARCEQUE_MINGA/frmPostulante.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

lista = []
class FormularioPostulante(QtWidgets.QMainWindow):

    def __init__(self):
        super(FormularioPostulante, self).__init__()
        uic.loadUi("EC2_FARCEQUE_MINGA/frmPostulante.ui", self)
        
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCerrar.clicked.connect(self.cerrar)
        
        self.show()
    
    def aceptar(self):
        # Entrada de datos
        nombre=""
        dni=""
        nombre=self.txtNombre.text()
        dni = self.txtDni.text()
        
        modalidad = self.cboModalidad.currentText()
        area = self.cboArea.currentText() 
        edad = int(self.spbEdad.value())
        
        # Condiciones de la modalidad
        iniciales = ""
        if modalidad == "Practicante":
            iniciales = "PR"
        if modalidad == "Medio Tiempo":
            iniciales = "MT"
        if modalidad == "Tiempo Completo":
            iniciales = "TC"
            
        # Condiciones del area
        carrera = ""
        if area == "Desarrollo de Sistemas":
            carrera = "DSI"
        if area == "Redes Informaticas":
            carrera = "RIN"
        if area == "Soporte Tecnico":
            carrera = "ST"
        # Condiciones de sexo
        genero = ""
        if self.rbMasculino.isChecked()==True: 
            
            femenino = ""
        if edad <23:
            genero = "FA"
        else:
            genero = "FB"
        if self.rbFemenino.isChecked()==True: 
           
            masculino = ""
        if edad <25:
            genero = "MA"
        else:
            genero = "MB"
        self.txtS.append("=======================".center(60))    
        self.txtS.append("|  CODIGO DEL POSTULANTE |".center(75))
        self.txtS.append("=======================".center(60))
        
        self.txtS.append("ALUMNO\t:"+str(nombre).upper()+"\n")
        self.txtS.append("CODIGO\t:"+ str(iniciales) + str(carrera) + str(genero) + str(dni).upper()+"\n")
    
    def cerrar(self):
        self.close()
        

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioPostulante()
    app.exec()