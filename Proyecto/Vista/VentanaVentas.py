from PyQt5 import QtWidgets, uic
from Controlador.ArregloClientes import *
from Controlador.ArregloProductos import *
from Vista.VentanaClientes import *
from Vista.VentanaProductos import *


aCli = ArregloClientes()

class VentanaVentas(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaVentas, self).__init__(parent)
        uic.loadUi("Proyecto/UI/VentanaVentas.ui", self)
        
        self.btnBuscarCliente.clicked.connect(self.buscarCliente)
        self.btnBuscarProducto.clicked.connect(self.buscarProducto)
        
        self.item = 0
        
    def buscarCliente(self):
        codigoCliente = self.txtCodigoCliente.text()
        if self.txtCodigoCliente.text() == "":
            QtWidgets.QMessageBox.information(self, "Codigo Cliente", "Debe ingresar el codigo del cliente...!!!", QtWidgets.QMessageBox.Ok)
        
        else:
            pos = aCli.buscarCliente(codigoCliente)
            objCliente = aCli.devolverCliente(pos)
            if pos == -1:
               QtWidgets.QMessageBox.information(self, "Codigo Cliente", "Cliete ", "Cliente no registrado...!!!", QtWidgets.QMessageBox.Ok)
            
            else:
              self.txtNombres.setText(objCliente.getNombre() + "" + objCliente.getApellidoPaterno() + "" +  objCliente.getApellidoMaterno())



    def buscarProducto(self):
        codigoProducto = self.txtCodigoProducto.text()
        if self.txtCodigoProducto.text() == "":
           QtWidgets.QMessageBox.information(self, "Codigo Producto", "Debe ingresar el codigo del producto...!!!", QtWidgets.QMessageBox.Ok)
        else: 
            pos = aPro.buscarProducto(codigoProducto)
            objProducto = aPro.devolverProducto(pos)
        if pos == -1:
            QtWidgets.QMessageBox.information(self, "Codigo Producto", "Producto no registrado...!!!", QtWidgets.QMessageBox.Ok)
            
        else:
            self.txtDescripcion.setText(objProducto. getDescripcion())
            self.txtStock.setText(objProducto. getStockActual())
            self.txtPrecio.setText(objProducto.getPrecioVenta())
            
    def obtenerNumeroDocumento(self):
        return self.txtNumeroDocumento.text()
    
    def obtenerCodigo(self):
        return self.txtCodigoProducto.text()
    
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
    
    def obtenerPrecio(self):
        return self.txtPrecio.text()
    
    def obtenerCantidad(self):
        return self.txtCantidad.text()
    
    def obtenerItem(self):
        self.item = self.item + 1 
        return self.item 
    
    def obtenerFecha(self):
        return self.txtFecha.text()
    
    
        
    
    
    
    
    
    
   
        

         