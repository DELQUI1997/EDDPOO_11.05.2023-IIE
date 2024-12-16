## Realizar un programa que tenga 1 función que permita dividir
# dos números enteros, a su vez deberá pedir dichos números enteros,
# el programa debe tener manejo de excepciones.
def division():
    try:
        a=int(input("ingresar valor 1 :"))
        b=int(input("ingresar valor 2 :"))
        div=a/b
        print("division",div)
    except ZeroDivisionError:
        print("no se puede dividir entre cero")
    except ValueError:
        print("valores ingresados son errados")
division()

    
    