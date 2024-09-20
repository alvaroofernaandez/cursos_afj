# EJERCICIO 4 IF

saldo = 2000

print ("---------MENÚ CAJERO---------\n")
print ("1. Ingresar dinero.")
print ("2. Retirar dinero.")
print ("3. Mostrar saldo actual.")
print ("4. Salir.")

print ("\n--\n")

opcion = int(input("Ingresa una opción: "))

if opcion == 1:
    dinero = float(input("¿Cuánto dinero quieres ingresar?: "))
    saldo = saldo + dinero
    print (f"Su saldo actual es: {saldo}")

elif opcion == 2:
    dinero = float(input("¿Cuánto dinero quieres retirar?: "))
    if dinero > saldo:
        print ("No tienes suficiente saldo para retirar este dinero")
    else:
        saldo = saldo - dinero
        print (f"Su saldo actual es: {saldo}")

elif opcion == 3:
    print (f"Su saldo actual es: {saldo}")

elif opcion == 4:
    print("Saliendo del programa...")

else:
    print ("Error")