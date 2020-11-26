#RECORRER UNA LISTA
#Puede recorrer los elementos de la lista mediante un for bucle:
#Imprima todos los elementos de la lista, uno por uno:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#Recorrer los números de índice
#También puede recorrer los elementos de la lista consultando su número de índice.
#Utilice las funciones range()y len()para crear un iterable adecuado.
#Imprima todos los elementos consultando su número de índice:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#Usar un bucle while
#Puede recorrer los elementos de la lista mediante un whilebucle.
#Utilice la len()función para determinar la longitud de la lista, luego comience en 0 y recorra los elementos de la lista consultando sus índices.
#Recuerde aumentar el índice en 1 después de cada iteración.
#Imprima todos los elementos, usando un whilebucle para revisar todos los números de índice

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Bucle con lista completa
#List Comprehensive ofrece la sintaxis más corta para recorrer listas:
#Imprima todos los elementos, usando un whilebucle para revisar todos los números de índice

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
  
  
