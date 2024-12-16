from  PyQt5 import QtWidgets, uic
from Controlador.ArregloProductos import *

# Instamciamos a las clasese arregloproductos, para utilizar sus atributos y metodos 
aPro = ArregloProductos()

class VentanaProductos(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("Proyecto/UI/VentanaProductos.ui", self)
        
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)            
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.listar()
        
    def obtenerCodigo(self):
        return self.txtCodigo.text()
    
    def obtenerNombre(self):
        return self.txtNombre.text()
    
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
    
    def obtenerMinimo(self):
        return self.txtStockMinimo.text()
    
    def obtenerActual(self):
        return self.txtStockActual.text()
    
    def obtenerCosto(self):
        return self.txtPrecioCosto.text()
    
    def obtenerVenta(self):
        return self.txtPrecioVenta.text()
    
    def obtenerProveedor(self):
        return self.cboProveedor.currentText()
    
    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()
    
    def limpiar(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)
    
    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Código del producto...!!!"
        if self.txtNombre.text() == "":
            self.txtNombre.setFocus()
            return "Nombre del producto...!!!"
        if self.txtDescripcion.text() == "":
            self.txtDescripcion.setFocus()
            return "Descripción del producto...!!!"
        if self.txtStockMinimo.text() == "":
            self.txtStockMinimo.setFocus()
            return "Stock Minimo del producto...!!!"
        if self.txtStockActual.text() == "":
            self.txtStockActual.setFocus()
            return "Stock Actual del producto...!!!"
        if self.txtPrecioCosto.text() == "":
            self.txtPrecioCosto.setFocus()
            return "precio costo del producto...!!!"
        if self.txtPrecioVenta.text() == "":
            self.txtPrecioVenta.setFocus()
            return "Precio venta del producto...!!!"
        if self.cboProveedor.currentText() == "Seleccionar Proveedor":
            self.cboProveedor.setCurrentIndex(0)
            return "Proveedor...!!!"
        if self.cboAlmacen.currentText() == "Seleccionar Almacen":
            self.cboAlmacen.setCurrentIndex(0)
            return "Almacen...!!!"
        else:
            return ""
            
    def listar(self):
        self.tblProductos.setRowCount(aPro.tamanoArregloProducto())
        self.tblProductos.setColumnCount(9)
        for i in range(aPro.tamanoArregloProducto()):
            self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCodigo()))
            self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getNombre()))
            self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getDescripcion()))
            self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockMinimo()))
            self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockActual()))
            self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioCosto()))
            self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioVenta()))
            self.tblProductos.setItem(i, 7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getProveedor()))
            self.tblProductos.setItem(i, 8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getAlmacen()))    
    
    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.clear()
        self.txtPrecioVenta.clear()
        self.cboProveedor.setCurrentIndex(0)
        self.cboAlmacen.setCurrentIndex(0)
        
    def registrar(self):
        if self.valida() == "":
            objPro = Producto(self.obtenerCodigo(), self.obtenerNombre(), self.obtenerDescripcion(), self.obtenerMinimo(), self.obtenerActual(), self.obtenerCosto(), self.obtenerVenta(), self.obtenerProveedor(), self.obtenerAlmacen())
            codigo = self.obtenerCodigo()
            if aPro.buscarProducto(codigo) == -1:
                aPro.adicionaProducto(objPro)
                aPro.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto", "El codigo ingresado ya existe...!!!" + self.valida(), QtWidgets.QMessageBox.Ok)
            
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
    
    
    
    def consultar(self):
        self.limpiar()
        if aPro.tamanoArregloProducto()==0:
            QtWidgets.QMessageBox.information(self,"Consultar Producto","No exiten productos a consultar..!!!!!",QtWidgets.QMessageBox.Ok)    
        else:
            codigo , _= QtWidgets.QInputDialog.getText(self,"Consultar Producto","Ingrese el codigo a consultar")
            pos = aPro.buscarProducto(codigo)        
            if pos==-1:
                QtWidgets.QMessageBox.information(self,"Consultar Producto","El codigo ingresado no existe ..!!!!!",QtWidgets.QMessageBox.Ok)    
            else:
                self.tblProductos.setRowCount(1)# asignar una fila para que en esa fila me asgine los productos
                self.tblProductos.setItem(0,0,QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getCodigo()))
                self.tblProductos.setItem(0,1,QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getNombre()))
                self.tblProductos.setItem(0,2,QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getDescripcion()))
                self.tblProductos.setItem(0,3,QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockMinimo()))
                self.tblProductos.setItem(0,4,QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockActual()))
                self.tblProductos.setItem(0,5,QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioCosto()))
                self.tblProductos.setItem(0,6,QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioVenta()))
                self.tblProductos.setItem(0,7,QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getProveedor()))
                self.tblProductos.setItem(0,8,QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getAlmacen()))   
    
    
    def eliminar(self):
        if aPro.tamanoArregloProducto() ==0:
            QtWidgets.QMessageBox.information(self, "eliminar Producto", "No Existen productos a Eliminar...!!!", QtWidgets.QMessageBox.Ok)
            
        else:
            fila = self.tblProductos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblProductos.item(indiceFila, 0).text()
                pos = aPro.buscarProducto(codigo)
                aPro.eliminarProducto(pos)
                aPro.grabar()  #ojo tener en cuenta
                self.limpiar()
                self.listar()
        
    def modificar(self):
        if aPro.tamanoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto", "No existen productos a modificar...!!!", QtWidgets.QMessageBox.Ok)

        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Modificar Producto", "Ingrese el código a modificar")
            pos = aPro.buscarProducto(codigo)
            if pos != -1:

                objProducto = aPro.devolverProducto(pos)
                self.btnModificar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtCodigo.setText(objProducto.getCodigo())
                self.txtCodigo.setVisible(False)
                self.txtCodigo.setVisible(False)
                self.txtNombre.setText(objProducto.getNombre())
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.txtStockMinimo.setText(objProducto.getStockMinimo())
                self.txtStockActual.setText(objProducto.getStockActual())
                self.txtPrecioCosto.setText(objProducto.getPrecioCosto())
                self.txtPrecioVenta.setText(objProducto.getPrecioVenta())
                self.cboProveedor.setCurrentText(objProducto.getProveedor())
                self.cboAlmacen.setCurrentText(objProducto.getAlmacen())      

   

    def grabar(self):

        pos = aPro.buscarProducto(self.obtenerCodigo())
        objProducto = aPro.devolverProducto(pos)
        objProducto.setNombre(self.obtenerNombre())
        objProducto.setDescripcion(self.obtenerDescripcion())
        objProducto.setStockMinimo(self.obtenerMinimo())
        objProducto.setStockActual(self.obtenerActual())
        objProducto.setPrecioCosto(self.obtenerCosto())
        objProducto.setPrecioVenta(self.obtenerVenta())
        objProducto.setProveedor(self.obtenerProveedor())
        objProducto.setAlmacen(self.obtenerAlmacen())
        self.btnModificar.setVisible(True)
        self.btnGrabar.setVisible(False)
        self.limpiar()
        self.limpiarControles()
        self.listar()
        self.txtCodigo.setVisible(True)
        self.txtCodigo.setVisible(True)   
        

        

