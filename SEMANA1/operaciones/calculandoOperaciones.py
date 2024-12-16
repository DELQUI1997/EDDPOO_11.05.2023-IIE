from operacionesBasicas import sumaTotal
from operacionesBasicas import restaTotal
from operacionesBasicas import multipTotal
from operacionesBasicas import dividirTotal
from operacionesBasicas import expon

n1 =float(input("Ingrese cualquier numero:"))
n2 =float(input("Ingrese cualquier numero:"))

print("LA SUMA ES\t\t:",sumaTotal(n1,n2))
print("LA RESTA ES\t\t:",restaTotal(n1,n2))
print("LA MULTIPLICACION ES\t:",multipTotal(n1,n2))
print("LA DIVISION ES\t\t:",dividirTotal(n1,n2))
print("LA POTENCIA ES\t\t:",expon(n1,n2))