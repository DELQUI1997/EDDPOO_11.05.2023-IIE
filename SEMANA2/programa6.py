# Realizar un programa que tenga 4 funciones que permita sumar, restar,
# multiplicar y dividir, a su vez deberá pedir dos números enteros, además
# de ingresar la operación que desea realizar, usando condicionales deberá 
# aplicar una de las operaciones, el programa debe tener manejo
# de excepciones.
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b 
def division(a,b):
    try :
        return a/b
    except ZeroDivisionError:
        print("no se puede dividir entre cero")
        return "operacion erronea"
while True:
    try:
        num1=int(input("ingrese el primer numero: "))       
        num2=int(input("ingrese el segundo numero: "))       
        break
    except ValueError:
        print("valores ingresados no correctos...!!!")
        print("intentelos nuevamente")
operacion=input("ingrese la operacion a realizar :\n-Suma\n-Resta\n-Multiplicacion\n-Division\n\n ").upper()
if  operacion=="SUMA":
    print(suma(num1,num2))
elif  operacion=="RESTA":
    print(resta(num1,num2))
elif operacion=="MULTIPLICACION" or operacion=="MULTIPLICACIÓN":
    print(multiplicacion(num1,num2))
elif operacion=="DIVISION":
    print(division(num1,num2))
else:
    print("operacion no comtenplada..")
        
        
    
