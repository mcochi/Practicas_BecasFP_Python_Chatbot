#ELIMINAR ARTICULO ESPECIFICADO
#El remove()método elimina el elemento especificado.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#ELIMINAR INDICE ESPECIFICADO
#El pop()método elimina el índice especificado.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Si no especifica el índice, el pop()método elimina el último elemento.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#La delpalabra clave también elimina el índice especificado:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#La delpalabra clave también puede eliminar la lista por completo.

thislist = ["apple", "banana", "cherry"]
del thislist


#BORRAR LA LISTA
#El clear()método vacía la lista.
#La lista aún permanece, pero no tiene contenido.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


