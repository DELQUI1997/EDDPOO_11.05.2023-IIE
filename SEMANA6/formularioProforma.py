import sys
from PyQt5 import QtWidgets, uic

qtCreatorFile = "SEMANA6/frmProforma.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class FormularioProforma(QtWidgets.QMainWindow):

    def __init__(self):
        super(FormularioProforma, self).__init__()
        uic.loadUi("SEMANA6/frmProforma.ui", self)
        
        
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show()
        
    def calcular(self):
        # Entrada de datos 
        precio = float(self.txtPrecio.text())
        cantidad = int(self.spbCantidad.value())
        
        # Proceso de calculo
        importe = precio * cantidad
        
        porcentajeDescuento=0
        if self.rbMayorista.isChecked()==True: #para preguntar si esta el boton seleccionado , isChecked
            porcentajeDescuento=4.5/100 #4.5%
        if self.rbMinorista.isChecked()==True: #para preguntar si esta el boton seleccionado , isChecked
            porcentajeDescuento=1.9/100 #4.5%
        descuento=importe*porcentajeDescuento    
            
        descuento = importe * porcentajeDescuento
        
        porcentajeInteres = 0
        if self.rbInteres1.isChecked() == True:
            porcentajeInteres = 0/100
        if self.rbInteres2.isChecked() == True:
            porcentajeInteres = 8.5/100
        if self.rbinteres3.isChecked() == True:
            porcentajeInteres = 12.5/100
        
        interes = importe * porcentajeInteres
        total = importe - descuento + interes
        
        # Salida de resultados 
        
        self.txtImporte.setText("S/. " + str("{:.2f}".format(importe)))
        self.txtDescuento.setText("S/. " + str("{:.2f}".format(descuento)))
        self.txtInteres.setText("S/. " + str("{:.2f}".format(interes)))
        self.txtTotal.setText("S/. " + str("{:.2f}".format(total)))
        
        
        codigo=""
        nombre=""
        producto=""
        codigo=self.txtCodigoCliente.text()
        nombre=self.txtNombreCliente.text()
        producto=self.txtProducto.text()
        
        self.txtS.setText("======================".center(60))
        self.txtS.append("|  PROFORMA |".center(75))
        self.txtS.append("=======================".center(60))
        
        
        self.txtS.append("CÓDIGO DEL CLIENTE\t:"+str(codigo).upper())
        self.txtS.append("NOMBRE DEL CLIENTE\t:"+str(nombre).upper()+"\n")
        self.txtS.append("PRODUCTO\t\t:"+str(producto).upper())
        
        self.txtS.append("PRECIO\t\t\t:"+"S/."+str("{:.2F}".format(precio)))
        self.txtS.append("CANTIDAD\t\t:"+str(cantidad))
        
        self.txtS.append("IMPORTE \t\t\t:"+"S/."+str("{:.2f}".format(importe)))
        self.txtS.append("DESCUENTO \t\t:"+"S/."+str("{:.2F}".format(descuento)))
        self.txtS.append("INTERES\t\t\t:"+"S/."+str("{:.2F}".format(interes)))
        self.txtS.append("TOTAL\t\t\t:"+"S/."+str("{:.2F}".format(total)))
        

    def limpiar(self):
        self.txtCodigoCliente.setText("")
        self.txtNombreCliente.setText("")
        self.txtProducto.setText("")
        self.txtPrecio.setText("")
        self.spbCantidad.setValue(0)
        self.txtImporte.setText("")
        self.txtDescuento.setText("")
        self.txtInteres.setText("")
        self.txtTotal.setText("")
        self.txtS.setText("")
        self.rbInteres1.setChecked(True)
        self.rbMayorista.setChecked(True)

    def salir(self):
        self.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormularioProforma()
    app.exec()
        