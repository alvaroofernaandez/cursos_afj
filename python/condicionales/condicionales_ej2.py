# EJERCICIO 2 IF

n1 = int(input("Ingresa un número: "))
print ("\n---\n")
n2 = int(input("Ingresa un segundo número: "))
print ("\n---\n")
n3 = int(input("Ingresa un tercer número: "))
print ("\n---\n")

if n1 >= n2 and n2 > n3:
    print (f"El número 1 es el mayor ({n1})")
elif n2 > n1 and n2 > n3:
    print (f"El número 2 es el mayor ({n2})")
elif n3 > n1 and n3 > n2:
    print (f"El número 3 es el mayor ({n3})")