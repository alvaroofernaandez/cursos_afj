# EJERCICIO 3 IF

nombre1 = input("Ingresa el primer nombre: ")
nombre2 = input("Ingresa el segundo nombre: ")

print("\n--\n")

if nombre1[0] == nombre2[0]:
    print(f"{nombre1} y {nombre2} comienzan con la misma letra")
elif nombre1[-1] == nombre2[-1]:
    print(f"{nombre1} y {nombre2} acaban con la misma letra")
else:
    print("No existe ninguna coincidencia.")    

print("\n--\n")

print("Finalizando programa...")