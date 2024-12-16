try: # cuando pase algun error aparece el mensaje "se produjo un error"
    a=5
    b='0' #no es un entero es un string
    print(a+b) #5+cadena 0
#value error cuando e colocado errores en los valores
#pero el error es cuando intentio hacer la suma
except TypeError:
    print("es una operacion no soportada...!!!!")

