cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual: "))
años = int(input("Introduce el número de años: "))

capital = cantidad * (1 + interes / 100) ** años

print("El capital obtenido en la inversión es:", capital)
