#Comprensión de listas
#La comprensión de listas ofrece una sintaxis más corta cuando desea crear una nueva lista
#basada en los valores de una lista existente.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Con la comprensión de listas, puede hacer todo eso con solo una línea de código:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#LA SINTAXIS
#newlist = [expression for item in iterable if condition == True]
#El valor de retorno es una nueva lista, dejando la lista anterior sin cambios.

#CONDICION
#La condición es como un filtro que acepta solo los artículos que valora True.

#Acepte solo artículos que no sean "apple":
newlist = [x for x in fruits if x != "apple"]


#La condición if x != "apple"  volverá Truepara todos los elementos que no sean "manzana", haciendo que la nueva lista contenga todas las frutas excepto "manzana".
#La condición es opcional y se puede omitir:

#Sin ifdeclaración:
newlist = [x for x in fruits]


#ITERABLE
#El iterable puede ser cualquier objeto iterable, como una lista, tupla, conjunto, etc.

#Puede usar la range()función para crear un iterable:
newlist = [x for x in range(10)]

#Mismo ejemplo, pero con una condición:
newlist = [x for x in range(10) if x < 5]


#EXPRESION
#La expresión es el elemento actual en la iteración, pero también es el resultado, que puede manipular antes de que termine como un elemento de lista en la nueva lista:


#stablezca los valores de la nueva lista en mayúsculas:
newlist = [x.upper() for x in fruits]

#stablezca todos los valores de la nueva lista en 'hola':
newlist = ['hello' for x in fruits]

#Devuelve "naranja" en lugar de "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]

#La expresión del ejemplo anterior dice:

#"Devuelve el artículo si no es banana, si es banana vuelve naranja"



