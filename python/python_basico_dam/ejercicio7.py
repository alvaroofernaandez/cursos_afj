peso = float(input("Introduce tu peso en kg (Introducir en decimales. Ej: 70.5): "))
estatura = float(input("Introduce tu estatura en metros (Introducir en decimales. Ej: 1.75): "))

imc = peso / (estatura**2)
imc = round(imc, 2)

print("Tu índice de masa corporal es", imc)
