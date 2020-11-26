#AGREGAR ELEMNTOS
#Para agregar un elemento al final de la lista, use el método append () :

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#INSERTAR ELEMNTOS
#Para insertar un elemento de lista en un índice específico, use el insert()método.
#El insert()método inserta un elemento en el índice especificado:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#Nota: Como resultado de los ejemplos anteriores, las listas ahora contendrán 4 elementos.


#AMPLIAR LISTA
#Para agregar elementos de otra lista a la lista actual, use el extend()método.
#Agregue los elementos de tropicala thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#AFGREGAR CUALQUIER ITERABLE
#El extend()método no tiene que agregar listas , puede agregar cualquier objeto iterable (tuplas, conjuntos, diccionarios, etc.).
#Agrega elementos de una tupla a una lista:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
