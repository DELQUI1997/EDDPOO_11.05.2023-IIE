try:
    a=5
    b=0
    print(a/b)

except TypeError:
    print("operacion no soportada !!!!")

except ZeroDivisionError:
    print("no se puede dividir por cero !!!!")