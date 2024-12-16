# Elabore un algoritmo que compruebe si una cadena leída por teclado comienza por una subcadena introducida por teclado.
cadena = input("Ingrese una caedna:")
subcadena = input("Ingrese una subcadena:")

if cadena.startswith(subcadena):
    print("La CADENA comienza por la SUBCADENA....!!")
else:
    print("La CADENA NO comienza por la SUBCADENA...!!")  