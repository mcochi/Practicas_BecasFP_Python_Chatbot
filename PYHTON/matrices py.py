#MATRICES DE PYTHON
#Nota: Python no tiene soporte integrado para Arrays, pero se pueden utilizar Python Lists en su lugar.

#MATRICES
#Nota: Esta página le muestra cómo usar LISTS como ARRAYS, sin embargo, para trabajar con arreglos en Python, tendrá que importar una biblioteca, como la biblioteca NumPy .

#Las matrices se utilizan para almacenar varios valores en una sola variable:

cars = ["Ford", "Volvo", "BMW"]
print(cars)

#Acceder a los elementos de una matriz
#Se refiere a un elemento de matriz refiriéndose al número de índice.

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)

#Modifique el valor del primer elemento de la matriz:

cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

print(cars)

#La longitud de una matriz
#Utilice el len()método para devolver la longitud de una matriz (el número de elementos en una matriz).

cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)
#Nota: La longitud de una matriz es siempre uno más que el índice de matriz más alto.

#Elementos de matriz en bucle
#Puede utilizar el for inbucle para recorrer todos los elementos de una matriz.

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)

#Agregar elementos de matriz
#Puede usar el append()método para agregar un elemento a una matriz.

cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)

#Eliminación de elementos de matriz
#Puede utilizar el pop()método para eliminar un elemento de la matriz.

cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)

#También puede utilizar el remove()método para eliminar un elemento de la matriz.

cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)
#Nota: El remove()método de la lista solo elimina la primera aparición del valor especificado.


