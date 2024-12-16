# Elabore un programa que pida una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.
cadena = input("Ingrese una cadena:")
while True:
    caracter = input("Ingrese un caracter:")
    if len(caracter)== 1: break
    
contador = cadena.count(caracter)
print("VECES:", contador)



    
