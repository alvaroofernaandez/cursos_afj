# EJERCICIO 1 IF

n1 = int(input("Ingresa un número: "))
print("\n---\n")
n2 = int(input("Ingresa otro número: "))
print("\n---\n")

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Ambos números son pares")
elif n1 % 2 == 0 and n2 % 2!= 0:
    print(f"El número 2 ({n2}) es impar")
elif n1 % 2!= 0 and n2 % 2 == 0:
    print(f"El número 1 ({n1}) es impar")
else:
    print("Ambos números son impares")

print("\n---\n")
print("Finalizando programa...")