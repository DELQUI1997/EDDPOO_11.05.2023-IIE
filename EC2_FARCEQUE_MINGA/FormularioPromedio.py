import sys
from PyQt5 import QtWidgets, uic
qtCreatorFile = "EC2_FARCEQUE_MINGA/frmPromedio.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

lista = []
class FormularioPromedio(QtWidgets.QMainWindow):

    def __init__(self):
        super(FormularioPromedio, self).__init__()
        uic.loadUi("EC2_FARCEQUE_MINGA/frmPromedio.ui", self)
        
        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnPromedio.clicked.connect(self.promedio)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show()
        
    def nuevo(self):
        self.txtApellidoNombre.clear()
        self.txtNota1.clear()
        self.txtNota2.clear()
        self.txtNota3.clear()
        self.txtExamenFinal.clear()
        self.txtPromedioFinal.clear()
        
    def promedio(self):
        #Datos de entrada
        nombre = self.txtApellidoNombre.text().upper()
        nota1 = float(self.txtNota1.text())
        nota2 = float(self.txtNota2.text())
        nota3 = float(self.txtNota3.text())
        exafinal = float(self.txtExamenFinal.text())
        
        #Condiciones de las notas 
        promedio = 0
        promedio = nota1 * 0.04 + nota2 * 0.12 + nota3 * 0.24 + exafinal * 0.60
        if promedio >= 12.5: 
            estado = "Aprobado"
        if promedio < 12.5: 
            estado = "Desaprobado"
        
        #datos de salida 
        self.txtPromedioFinal.setText(str(promedio))
        notas = (nombre, str(nota1), str(nota2),str(nota3), str(exafinal),str(promedio),estado)
        lista.append(notas)
        self.listar()
         
    def listar(self):
        self.tblDatos.setRowCount(50)
        for i in range(len(lista)):
            self.tblDatos.setItem(i, 0, QtWidgets.QTableWidgetItem(lista[i][0]))
            self.tblDatos.setItem(i, 1, QtWidgets.QTableWidgetItem(lista[i][1]))
            self.tblDatos.setItem(i, 2, QtWidgets.QTableWidgetItem(lista[i][2]))
            self.tblDatos.setItem(i, 3, QtWidgets.QTableWidgetItem(lista[i][3]))
            self.tblDatos.setItem(i, 4, QtWidgets.QTableWidgetItem(lista[i][4]))
            self.tblDatos.setItem(i, 5, QtWidgets.QTableWidgetItem(lista[i][5]))
            self.tblDatos.setItem(i, 6, QtWidgets.QTableWidgetItem(lista[i][6]))
         
    def salir(self):
        self.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioPromedio()
    app.exec()
        
