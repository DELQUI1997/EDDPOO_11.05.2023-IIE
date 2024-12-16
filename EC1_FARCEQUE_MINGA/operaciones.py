#SUMA
def suma(a, b):
    return a + b
#RESTA
def restar(a, b):
    return a - b
#MULTIPLICACION
def multiplicar(a, b):
    return a * b
#POTENCIA
def potencia(a, b):
    return a ** b
#DIVISION
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        ("Error al dividir entre 0 ..!!!")
        return   "Operacion erronea"

while True:
    try:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print("Numeros ingresados incorrectos")
        
        print("Ingrese nuevamente el numero")
        
operacion = input("Ingresa la operacion a realizar: \n- suma\n- restar\n- multiplicar\n- potencia\n- dividir\n>").upper()

if operacion =="SUMA":
    print("SUMA: ", suma(num1, num2))

elif operacion =="RESTAR":
    print("RESTAR: ", restar(num1, num2))

elif operacion =="MULTIPLICAR":
    print("MULTIPLICAR: ", multiplicar(num1, num2))
    
elif operacion =="POTENCIA":
    print("POTENCIA: ", potencia(num1, num2))

elif operacion =="DIVIDIR":
    print("DIVIDIR: ", dividir(num1, num2))
    
else:
    print("Completa la operacion")
