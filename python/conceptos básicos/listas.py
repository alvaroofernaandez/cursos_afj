#             LISTAS - ARRAYS

# Listas:

array1=["futbol", "pc", 18.6, 18, [7,8,10.4], True, False, "pc"]
array2=[200, 250, "hola como estas"]
array3=array1+array2
print(array1)

print("\n------------------------------------------------\n")

print(array1[4])

print("\n------------------------------------------------\n")

print(array1[0:2]) # ---> Para pedir los dos pirmeros datos

print("\n------------------------------------------------\n")

# Funciones en listas:

print(len(array1), "<--- Esta es la cantidad de datos que hay en la lista")
print("\n--\n")

array1.append(66) # Añade un elemento a la lista
print(array1)

print("\n--\n")

array1.insert(1, "ruben") # Añade un elemento a la lista desde la posicion que deseas
print(array1)

print("\n--\n")

array1.extend([1, 892, True, 101.23])
print(array1)

print("\n--\n")

print(array3)

print("\n--\n")

print("pc" in array1) # ---> Verifica si un elemento existe en la lista
print(array1.index("pc")) # ---> Verifica donde se encuentra un elemento en la lista
print(array1.count("pc")) # ---> Verifica cuantas veces se encuentra un elemento o valor en la lista
array1.remove(True) # ---> Elimina un elemento de la lista
print(array1)
array1.clear() # ---> Elimina todos los elementos de la lista
array1.reverse() # ---> Invertir el orden de la lista

print("\n------------------------------------------------\n")

array=[1, 2, 4, 6, -13]
array.sort() # ---> Ordena la lista de forma ascendente
print(array)

