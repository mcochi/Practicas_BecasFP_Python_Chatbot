#TUPLA
#Una tupla es una colección ordenada e inmutable .
#En Python, las tuplas se escriben entre paréntesis.

thistuple = ("apple", "banana", "cherry")
print(thistuple)


#Acceder a elementos de tupla
#Puede acceder a elementos de tupla consultando el número de índice, entre corchetes:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])                      #2 objeto de la tupla


#Indexación negativa
#La indexación negativa significa comenzar desde el final, se -1refiere al último elemento,
#se -2refiere al penúltimo elemento, etc.

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Rango de índices
#Puede especificar un rango de índices especificando dónde comenzar y dónde terminar el rango.
#Al especificar un rango, el valor de retorno será una nueva tupla con los elementos especificados.


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#Nota: La búsqueda comenzará en el índice 2 (incluido) y terminará en el índice 5 (no incluido).
#Recuerde que el primer elemento tiene índice 0.

#Rango de índices negativos
#Especifique índices negativos si desea iniciar la búsqueda desde el final de la tupla:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#Cambiar valores de tupla
#Una vez que se crea una tupla, no puede cambiar sus valores. Las tuplas son inmutables o inmutables, como también se las llama.
#Pero hay una solución. Puede convertir la tupla en una lista, cambiar la lista y volver a convertir la lista en una tupla.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Bucle a través de una tupla
#Puede recorrer los elementos de la tupla utilizando un forbucle.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Compruebe si el artículo existe
#Para determinar si un elemento específico está presente en una tupla, use la inpalabra clave:
  
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


#Longitud de la tupla
#Para determinar cuántos elementos tiene una tupla, use el len()método:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#Crear tupla con un elemento
#Para crear una tupla con un solo elemento, debe agregar una coma después del elemento; de lo contrario, Python no lo reconocerá como una tupla.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Eliminar elementos
#Nota: no puede eliminar elementos en una tupla.
#Las tuplas no se pueden cambiar , por lo que no puede eliminar elementos de ellas, pero puede eliminarlas por completo:

#thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists


#Unir dos tuplas
#Para unir dos o más tuplas, puede utilizar el + operador:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

#El constructor tuple ()
#También es posible usar el constructor tuple () para hacer una tupla.

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#METODOS

#Method	Description
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found






