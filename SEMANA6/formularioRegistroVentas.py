import sys
from PyQt5 import QtWidgets, uic
from datetime import date


qtCreatorFile = "SEMANA6/frmRegistroVentas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

lista = []
class FormularioRegistroVentas(QtWidgets.QMainWindow):
    

    def __init__(self):
        super(FormularioRegistroVentas, self).__init__()
        uic.loadUi("SEMANA6/frmRegistroVentas.ui", self)
        
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show()
        
    def registrar(self):
        #Entrada de datos
        dia = self.dtFecha.date().day()
        mes = self.dtFecha.date().month()
        ano = self.dtFecha.date().year()
        fecha = str(dia) + "/" + str(mes) + "/" + str(ano)
        

        producto = self.cboProducto.currentText()
        tipoPago = self.cboPago.currentText()  
        cantidad = int(self.txtCantidad.text())
        
        #Mostrar precio del producto
        precio = 0
        if producto == "Coleccion Escolar":
            precio = 240
        if producto == "Coleccion PreUniversitaria":
            precio = 150
        if producto == "Coleccion Profesional":
            precio = 350
            
        self.lblPrecio.setText("S/. " + str(precio))
        
        #Calculando el subtotal
        subtotal = precio * cantidad
        
        #Calculando el descuento y el recargo
        descuento = 0
        recargo = 0
        if tipoPago == "Contado":
            descuento = 0.05 * subtotal
        if tipoPago == "Tarjeta de Credito":
            recargo = 0.10 * subtotal
            
        # Calculando el precio final
        precioFinal = subtotal - descuento + recargo
        
        # Agregando datos a la lista y mostrrar datos en la tabla
        datos = (producto, str(cantidad), "S/. " + str(precio), tipoPago,
        "S/. " + str(descuento), "S/. " + str(recargo), "S/. " + str(precioFinal), fecha)
        lista.append(datos)
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
            self.tblDatos.setItem(i, 7, QtWidgets.QTableWidgetItem(lista[i][7]))      
        
    def nuevo(self):
        self.txtCantidad.clear()
        self.lblPrecio.clear()
        self.cboProducto.setCurrentIndex(0)
        self.cboPago.setCurrentIndex(0)
        
    def salir(self):
        self.close()
         
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioRegistroVentas()
    app.exec()
        