from PyQt5 import QtWidgets, uic
from Controlador.ArregloClientes import *

# Instanciamos a la clase ArregloClientes, para utilizar sus atributos y métodos

aCli = ArregloClientes()

class VentanaClientes(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaClientes, self).__init__(parent)
        uic.loadUi("Proyecto/UI/VentanaClientes.ui", self)


        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnListar.clicked.connect(self.listar)
        self.listar()

    def obtenerDni(self):
        return self.txtDni.text()

    def obtenerNombres(self):
        return self.txtNombres.text()

    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()

    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()

    def obtenerDireccion(self):
        return self.txtDireccion.text()

    def obtenerTelefono(self):
        return self.txtTelefono.text()

    def limpiarTabla(self):
        self.tblClientes.clearContents()
        self.tblClientes.setRowCount(0)

    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del cliente...!!!"

        if self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombres del cliente...!!!"

        if self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del cliente...!!!"

        if self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del cliente...!!!"

        if self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Dirección del cliente...!!!"

        if self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Teléfono del cliente...!!!"
        else:
            return ""

    def listar(self):
        self.tblClientes.setRowCount(aCli.tamanoArregloCliente())
        self.tblClientes.setColumnCount(6)
        for i in range(aCli.tamanoArregloCliente()):
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDni()))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getNombre()))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoPaterno()))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoMaterno()))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDireccion()))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getTelefono()))

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

    def registrar(self):
        if self.valida() == "":
            objCli = Cliente(self.obtenerDni(), self.obtenerNombres(), self.obtenerApellidoPaterno(), self.obtenerApellidoMaterno(), self.obtenerDireccion(), self.obtenerTelefono())
            dni = self.obtenerDni()
            if aCli.buscarCliente(dni) == -1:
                aCli.adicionaCliente(objCli)
                aCli.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "El dni ingresado ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)


    def consultar(self):
        self.limpiarTabla()
        if aCli.tamanoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Cliente", "No existen clientes a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Cliente", "Ingrese el dni a consultar")
            pos = aCli.buscarCliente(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente", "El dni ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.tblClientes.setRowCount(1)
                self.tblClientes.setItem(0, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDniCliente()))
                self.tblClientes.setItem(0, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getNombresCliente()))
                self.tblClientes.setItem(0, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoPaternoCliente()))
                self.tblClientes.setItem(0, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoMaternoCliente()))
                self.tblClientes.setItem(0, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDireccionCliente()))
                self.tblClientes.setItem(0, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getTelefonoCliente()))

             

   

    def eliminar(self):
        if aCli.tamanoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "No existen clientes a eliminar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblClientes.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                dni = self.tblClientes.item(indiceFila, 0).text()
                pos = aCli.buscarCliente(dni)
                aCli.eliminarCliente(pos)
                aCli.grabar()
                self.limpiarTabla()
                self.listar()

            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "Debe seleccionar una fila...!!!", QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aCli.tamanoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "No existen clientes a modificar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Modificar Cliente", "Ingrese el dni a modificar")
            pos = aCli.buscarCliente(dni)
            if pos != -1:
                objCliente = aCli.devolverCliente(pos)
                self.btnModificar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtDni.setText(objCliente.getDniCliente())
                self.txtDni.setVisible(False)
                self.lblDni.setVisible(False)
                self.txtNombres.setText(objCliente.getNombresCliente())
                self.txtApellidoPaterno.setText(objCliente.getApellidoPaternoCliente())
                self.txtApellidoMaterno.setText(objCliente.getApellidoMaternoCliente())
                self.txtDireccion.setText(objCliente.getDireccionCliente())
                self.txtTelefono.setText(objCliente.getTelefonoCliente())

    def grabar(self):
        pos = aCli.buscarCliente(self.obtenerDni())
        objCliente = aCli.devolverCliente(pos)
        objCliente.setNombresCliente(self.obtenerNombres())
        objCliente.setApellidoPaternoCliente(self.obtenerApellidoPaterno())
        objCliente.setApellidoMaternoCliente(self.obtenerApellidoMaterno())
        objCliente.setDireccionCliente(self.obtenerDireccion())
        objCliente.setTelefonoCliente(self.obtenerTelefono())
        self.btnModificar.setVisible(True)
        self.btnGrabar.setVisible(False)
        self.limpiarTabla()
        self.limpiarControles()
        self.listar()
        self.txtDni.setVisible(True)
        self.lblDni.setVisible(True)
        
   