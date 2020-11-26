#ACCESS ITEMS
#Los elementos de la lista están indexados y puede
#acceder a ellos consultando el número de índice

thislist = ["apple", "banana", "cherry"]
print(thislist[1])                        #Nota: El primer elemento tiene índice 0. osea apple


#INDEXACION NEGATIVA
#La indexación negativa significa comenzar desde el final
#-1se refiere al último elemento, se -2refiere al penúltimo elemento, etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])                       #ultimo elemnto de la lista


#RANGO DE INDICES
#Puede especificar un rango de índices especificando dónde comenzar y dónde terminar el rango.
#Al especificar un rango, el valor de retorno será una nueva lista con los elementos especificados.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Nota: La búsqueda comenzará en el índice 2 (incluido) y terminará en el índice 5 (no incluido).

#Al omitir el valor inicial, el rango comenzará en el primer elemento:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#Al omitir el valor final, el rango continuará hasta el final de la lista:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


#RANGO DE INDICES NEGATIVOS
#Especifique índices negativos si desea iniciar la búsqueda desde el final de la lista:
#Este ejemplo devuelve los elementos de "naranja" (-4) a, pero NO incluidos. "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


#COMPRUEBE SI EL ARTICULO EXISTE
#Para determinar si un elemento específico está presente en una lista, use la inpalabra clave:
#Compruebe si "manzana" está presente en la lista:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

