from PyQt5 import QtWidgets, uic
from Controlador.ArregloAlumnos import *

# Instanciamos a la clase ArregloClientes, para utilizar sus atributos y métodos

aAlu = ArregloAlumnos()

class VentanaAlumnos(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaAlumnos, self).__init__(parent)
        uic.loadUi("Proyecto/UI/VentanaAlumnos.ui", self)


        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnBuscar.clicked.connect(self.buscar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnListar.clicked.connect(self.listar)
        self.listar()

    def obtenerCodigo(self):
        return self.txtCodigo.text()

    def obtenerNombres(self):
        return self.txtNombres.text()

    def obtenerApellidos(self):
        return self.txtApellidos.text()

    def obtenerCiclo(self):
        return self.txtCiclo.text()

    def obtenerPension(self):
        return self.txtPension.text()

    def obtenerCarrera(self):
        return self.txtCarrera.text()
    
    def obtenerSede(self):
        return self.txtSede.text()

    def limpiarTabla(self):
        self.tblAlumnos.clearContents()
        self.tblAlumnos.setRowCount(0)

    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Codigo del alumno...!!!"

        if self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombres del alumno...!!!"

        if self.txtApellidos.text() == "":
            self.txtApellidos.setFocus()
            return "Apellido Paterno del alumno...!!!"

        if self.txtCiclo.text() == "":
            self.txtCiclo.setFocus()
            return "Ciclo del alumno...!!!"

        if self.txtPension.text() == "":
            self.txtPension.setFocus()
            return "Pension del alumno...!!!"

        if self.txtCarrera.text() == "":
            self.txtCarrera.setFocus()
            return "Carrera del alumno...!!!"
        
        if self.txtSede.text() == "":
            self.txtSede.setFocus()
            return "Sede del alumno...!!!"
        
        else:
            return ""

    def listar(self):
        self.tblAlumnos.setRowCount(aAlu.tamanoArregloAlumno())
        self.tblAlumnos.setColumnCount(6)
        for i in range(aAlu.tamanoArregloAlumno()):
            self.tblAlumnos.setItem(i, 0, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getCodigo()))
            self.tblAlumnos.setItem(i, 1, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getNombres()))
            self.tblAlumnos.setItem(i, 2, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getApellidos()))
            self.tblAlumnos.setItem(i, 3, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getCiclo()))
            self.tblAlumnos.setItem(i, 4, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getPension()))
            self.tblAlumnos.setItem(i, 5, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getCarrera()))
            self.tblAlumnos.setItem(i, 6, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(i).getSede()))

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombres.clear()
        self.txtApellidos.clear()
        self.txtCiclo.clear()
        self.txtPension.clear()
        self.txtCarrera.clear()
        self.txtSede.clear()

    def registrar(self):
        if self.valida() == "":
            objAlu = Alumno(self.obtenerCodigo(), self.obtenerNombres(), self.obtenerApellidos(), self.obtenerCiclo(), self.obtenerPension(), self.obtenerCarrera(), self.obtenerSede())
            codigo = self.obtenerCodigo()
            if aAlu.buscarAlumno(codigo) == -1:  #ojo
                aAlu.adicionaAlumno(objAlu)
                aAlu.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "El dni ingresado ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)


    def buscar(self):
        self.limpiarTabla()
        if aAlu.tamanoArregloAlumno() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Cliente", "No existen clientes a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Cliente", "Ingrese el dni a consultar")
            pos = aAlu.buscarAlumno(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente", "El dni ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.tblAlumnos.setRowCount(1)
                self.tblAlumnos.setItem(0, 0, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(pos).getCodigoAlumno()))
                self.tblAlumnos.setItem(0, 1, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(pos).getNombresAlumno()))
                self.tblAlumnos.setItem(0, 2, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(pos).getApellidos()))
                self.tblAlumnos.setItem(0, 3, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(pos).getCiclo()))
                self.tblAlumnos.setItem(0, 4, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(pos).getPension()))
                self.tblAlumnos.setItem(0, 5, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(pos).getCarrera()))
                self.tblAlumnos.setItem(0, 6, QtWidgets.QTableWidgetItem(aAlu.devolverAlumno(pos).getSede()))

             

   

    def eliminar(self):
        if aAlu.tamanoArregloAlumno() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "No existen clientes a eliminar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblAlumnos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblAlumnos.item(indiceFila, 0).text()
                pos = aAlu.buscarAlumno(codigo)  # ojojo
                aAlu.eliminarAlumno(pos)
                aAlu.grabar()
                self.limpiarTabla()
                self.listar()

            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "Debe seleccionar una fila...!!!", QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aAlu.tamanoArregloAlumno() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "No existen clientes a modificar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Modificar Cliente", "Ingrese el dni a modificar")
            pos = aAlu.buscarAlumno(codigo) # ojo
            if pos != -1:
                objAlumno = aCli.devolverAlumno(pos)
                self.btnModificar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtCodigo.setText(objAlumno.getCodigo())
                self.txtCodigo.setVisible(False)
                self.lblCodigo.setVisible(False)
                self.txtNombres.setText(objAlumno.getNombres())
                self.txtApellidos.setText(objAlumno.getApellidos())
                self.txtCiclo.setText(objAlumno.getCiclo())
                self.txtPension.setText(objAlumno.getPension())
                self.txtCarrera.setText(objAlumno.getCarrera())
                self.txtSede.setText(objAlumno.getSede())

    def grabar(self):
        pos = aAlu.buscarAlumno(self.obtenerCodigo())
        objAlumno = aAlu.devolverAlumno(pos)
        objAlumno.setNombres(self.obtenerNombres())
        objAlumno.setApellidos(self.obtenerApellidos())
        objAlumno.setCiclo(self.obtenerCiclo())
        objAlumno.setPension(self.obtenerPension())
        objAlumno.setCarrera(self.obtenerCarrera())
        objAlumno.setSede(self.obtenerSede())
        self.btnModificar.setVisible(True)
        self.btnGrabar.setVisible(False)
        self.limpiarTabla()
        self.limpiarControles()
        self.listar()
        self.txtCodigo.setVisible(True)
        self.lblCodigo.setVisible(True)      