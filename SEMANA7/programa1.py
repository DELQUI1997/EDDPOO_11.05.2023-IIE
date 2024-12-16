class Entidad:
    def __init__(self):
        self.razon_social = input("INGRESE RAZON SOCIAL\t:  ")
        self.ruc = int(input("INGRESE NUMERO DE RUC\t:  "))

    def mostrarDatos(self):
        print("RAZON SOACIAL\t\t: ", self.razon_social)
        print("RUC\t\t\t: ", self.ruc)


class Banco(Entidad):
    def __init__(self):
        super().__init__()
        self.deposito = 5000.0
        self.interes = 20 
        saldo = (self.deposito * self.interes /100) + self.deposito
        self.saldo = saldo
        
    def mostrarDatos(self):
        super().mostrarDatos()
        print("DEPOSITO\t\t:  S/.", self.deposito)
        print("INTERES\t\t\t: ", self.interes,("%"))
        print("SALDO\t\t\t:  S/.", self.saldo)
 
class Financiera(Entidad):
    def __init__(self):
        super().__init__()
        self.prestamo =  5000.0
        self.cobro_operacion = 100
        monto_prestamo = (self.prestamo - self.cobro_operacion)
        self.monto_prestamo = monto_prestamo
        
    def mostrarDatos(self):
        super().mostrarDatos()
        print("PRESTAMO\t\t:  S/.", self.prestamo)
        print("COBRO POR OPERACION\t:  S/.", self.cobro_operacion)
        print("MONTO DE PRESTAMO\t:  S/.", self.monto_prestamo)


entidad1 = Entidad()
entidad1.mostrarDatos()

print("+======================================================+")
print("|                     CLASE BANCO                      |")
print("+======================================================+")
banco1 = Banco()
banco1.mostrarDatos()

print("+======================================================+")
print("|                 CLASE FINANCIERA                     |")
print("+======================================================+")
financiera1 = Financiera()
financiera1.mostrarDatos()

