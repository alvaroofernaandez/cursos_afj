#     EJERCICIO 4

precio = float(input("Ingresa el precio del producto: "))
print("")

print("------------------------------------------------")

descuento = precio * (0.36)
precio = precio - descuento
print("¡Se ha aplicado un descuento del 36%!")
print("")

print("------------------------------------------------")

print(f"El precio final del producto es: {precio:.2f}€ ")