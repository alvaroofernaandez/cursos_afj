#                BUCLES

# BUCLE WHILE:

numero = 0

while numero < 20: 
    numero+=1
    print(numero)

print("\n----\n")       

import math
num = int(input("Ingrese un numero: "))

while num < 0:
    print("Por favor, ingrese un numero positivo: ")
    num = int(input("Ingrese un numero positivo: "))
print(f"La raiz cuadrada de {num} es: {math.sqrt(num):.2f}")

print("\n----\n")

#----------------------------------------------------------------

# BUCLE FOR:

datos=[6, 7, 8, 9, 10, "hola"]
for i in datos:
    print(f"Objeto: {i}")

