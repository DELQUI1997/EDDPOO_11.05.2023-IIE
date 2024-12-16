from Controlador.Clientes import Cliente

class ArregloClientes:
    
    def __init__(self):
        self.dataClientes = []
        self.cargar()
     
    def cargar(self):
        archivo = open("Proyecto/Modelo/Clientes.txt", "r")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            dni = columna [0]
            nombre = columna [1]
            apellidoPaterno = columna [2]
            apellidoMaterno = columna [3]
            direccion = columna [4]
            telefono = columna [5].strip()
            objCli = Cliente(dni, nombre, apellidoPaterno, apellidoMaterno, direccion, telefono)
            self.adicionaCliente(objCli)
        archivo.close()
        
        
    def grabar(self):
        archivo = open ("Proyecto/Modelo/Clientes.txt", "w")
        for i in range (self.tamanoArregloCliente()):
            archivo.write(str(self.devolverCliente(i).getDni()) + ","
                          + str(self.devolverCliente(i).getNombre()) + ","
                          + str(self.devolverCliente(i).getApellidoPaterno()) + ","
                          + str(self.devolverCliente(i).getApellidoMaterno()) + ","
                          + str(self.devolverCliente(i).getDireccion()) + ","
                          + str(self.devolverCliente(i).getTelefono()) + "\n")
        archivo.close()
                          
                          
                        
        
            
    
            
    def adicionaCliente(self, objCli):
        self.dataClientes.append(objCli)
        
    def devolverCliente(self, pos):
        return self.dataClientes[pos]
    
    def tamanoArregloCliente(self):
        return len(self.dataClientes)
    
    def buscarCliente(self, dni):
        for i in range(self.tamanoArregloCliente()):
            if dni == self.dataClientes[i].getDni():
                return i
        return -1
    
    def eliminarCliente(self, indice):
        del(self.dataClientes[indice])