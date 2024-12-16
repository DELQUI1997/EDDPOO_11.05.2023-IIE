#Realizar u  programa que simule tirar dos dados y lugo muestre los valores que aparecieron. Si la suma de dichos numeros es igual a 9 mostrar un mensaje de "Has ganada" sino "Has perdido"

# FORMA 1: USANDO EL PRIMER METODO DE IMPORTACION 

import random

num1 = random.randint(1,6)
num2 = random.randint(1,6)
suma = num1 + num2

print("PRIMER DADO\t: ",num1)
print("SEGUNDO DADO\t:",num2)
print("SUMA\t\t:",suma)

if suma == 9:
    print("HAS GANADAO...!!!!")
else:
    print("HAS PERDIDO...!!!")
    
# FROMA 2: USANDO EL SEGUNDO METODO DE IMPORTACION 

from random import randint 

num1 = randint(1,6)
num2 = randint(1,6)
suma = num1 + num2

print("PRIMER DADO\t: ",num1)
print("SEGUNDO DADO\t:",num2)
print("SUMA\t\t:",suma)

if suma == 9:
    print("HAS GANADAO...!!!!")
else:
    print("HAS PERDIDO...!!!")