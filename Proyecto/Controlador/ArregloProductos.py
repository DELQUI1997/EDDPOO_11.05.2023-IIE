from Controlador.Productos import Producto

class ArregloProductos:
    
    def __init__(self):
        self.dataProductos = []
        self.cargar()
     
    def cargar(self):
        archivo = open("Proyecto/Modelo/Productos.txt", "r")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna [0]
            nombre = columna [1]
            descripcion = columna [2]
            stock_minimo = columna [3]
            stock_actual = columna [4]
            precio_costo = columna [5]
            precio_venta = columna [6]
            proveedor = columna [7]
            almacen = columna [8].strip()
            objPro = Producto(codigo, nombre, descripcion, stock_minimo, stock_actual, precio_costo, precio_venta, proveedor, almacen)
            self.adicionaProducto(objPro)
        archivo.close()
        
        
    def grabar(self):
        archivo = open ("Proyecto/Modelo/Productos.txt", "w")
        for i in range (self.tamanoArregloProducto()):
            archivo.write(str(self.devolverProducto(i).getCodigo()) + ","
                          + str(self.devolverProducto(i).getNombre()) + ","
                          + str(self.devolverProducto(i).getDescripcion()) + ","
                          + str(self.devolverProducto(i).getStockMinimo()) + ","
                          + str(self.devolverProducto(i).getStockActual()) + ","
                          + str(self.devolverProducto(i).getPrecioCosto()) + ","
                          + str(self.devolverProducto(i).getPrecioVenta()) + ","
                          + str(self.devolverProducto(i).getProveedor()) + ","
                          + str(self.devolverProducto(i).getAlmacen()) + "\n")
        archivo.close()
                          
                          
                        

    def adicionaProducto(self, objPro):
        self.dataProductos.append(objPro)
        
    def devolverProducto(self, pos):
        return self.dataProductos[pos]
    
    def tamanoArregloProducto(self):
        return len(self.dataProductos)
    
    def buscarProducto(self, codigo):
        for i in range(self.tamanoArregloProducto()):
            if codigo == self.dataProductos[i].getCodigo():
                return i
        return -1
    
    def eliminarProducto(self, indice):
        del(self.dataProductos[indice])
        
        
        
        
        
        
        
"""
dataProductos = [
    ["P001", "Teclado", "Teclado hp", 100, 150, 80, 120, proveedor, Almacen1]
    ["P001", "Impresora", "Impresora hp", 100, 150, 80, 120, proveedor, Almacen2]
    ["P001", "usb", "usb 32 gb", 100, 150, 80, 120, proveedor, Almacen2]
    ["P001", "monitor", "monitor sonic", 100, 150, 80, 120, proveedor, Almacen2]
"""   
    