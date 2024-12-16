from areaCuadrado import cuadrado
from areaRectangulo import rectangulo
from areaTrapecio import trapecio

print("\n=================")
print("AREA DEL CUADRADO")
print("=================\n")

lado = float(input("Ingrese el lado del cuadrado:"))
print("AREA DEL CUADRAADO:",cuadrado(lado))

print("\n=================")
print("AREA DEL RECTANGULO")
print("=================\n")

base = float(input("Ingrese la base del rectangluo:"))
altura = float(input("Ingrese la altura del rectangulo:"))
print("AREA DEL RECTANGULO:",rectangulo(base , altura))

print("\n=================")
print("AREA DEL TRAPECIO")
print("=================\n")

baseMayor = float(input("Ingrese la base mayor del trapecio:"))
baseMenor = float(input("Ingrese la base Menor del trapecio:"))
altura = float(input("Ingrese la altura del trapecio:"))
print("AREA DEL TRAPECIO",trapecio(baseMayor , baseMenor , altura))
