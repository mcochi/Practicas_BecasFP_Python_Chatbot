#Conjuntos de Python
#Un conjunto es una colección que no está ordenada ni indexada. En Python, los conjuntos se escriben con llaves.

thisset = {"apple", "banana", "cherry"}
print(thisset)
#Nota: Los conjuntos están desordenados, por lo que no puede estar seguro en qué orden aparecerán los elementos.


#Elementos de acceso
#No puede acceder a los elementos de un conjunto consultando un índice o una clave.
#Pero puede recorrer los elementos del conjunto usando un for ciclo, o preguntar si un valor específico está presente en un conjunto, usando la inpalabra clave.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#Compruebe si "banana" está presente en el conjunto:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


#Cambiar elementos
#Una vez que se crea un conjunto, no puede cambiar sus elementos, pero puede agregar elementos nuevos.


#Agregar elementos
#Para agregar un artículo a un conjunto, use el add() método.
#Para agregar más de un elemento a un conjunto, use el update() método.

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#Obtenga la longitud de un conjunto
#Para determinar cuántos elementos tiene un conjunto, use el len()método.

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Remover el artículo
#Para eliminar un elemento de un conjunto, utilice remove()el discard()método o el .

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#Nota: Si el elemento a eliminar no existe, remove()generará un error.

#Quite "banana" usando el discard() método:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#Nota: Si el elemento a eliminar no existe, NOdiscard() generará un error.
#También puede utilizar el pop()método, para eliminar un elemento, pero este método eliminará el último elemento. Recuerde que los conjuntos están desordenados, por lo que no sabrá qué elemento se quita.
#El valor de retorno del pop()método es el elemento eliminado.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#Nota: Los conjuntos están desordenados , por lo que cuando utilice el pop()método, no sabrá qué elemento se elimina.

#El clear() método vacía el conjunto:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#La delpalabra clave eliminará el conjunto por completo:

#thisset = {"apple", "banana", "cherry"}
#del thisset
#print(thisset)

#Unir dos conjuntos
#Hay varias formas de unir dos o más conjuntos en Python.
#Puede utilizar el union()método que devuelve un nuevo conjunto que contiene todos los elementos de ambos conjuntos, o el update()método que inserta todos los elementos de un conjunto en otro:
#El union()método devuelve un nuevo conjunto con todos los elementos de ambos conjuntos:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#El update()método inserta los elementos de set2 en set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Nota: Ambos union()y update() excluirán cualquier artículo duplicado.

#El constructor set ()
#También es posible usar el constructor set () para hacer un conjunto.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#Establecer métodos

#Method	                            Description
#add()	                            Adds an element to the set
#clear()	                            Removes all the elements from the set
#copy()	                            Returns a copy of the set
#difference()	                    Returns a set containing the difference between two or more sets
#difference_update()	            Removes the items in this set that are also included in another, specified set
#discard()	                    Remove the specified item
#intersection()	                    Returns a set, that is the intersection of two other sets
#intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	                    Returns whether two sets have a intersection or not
#issubset()	                    Returns whether another set contains this set or not
#issuperset()	                    Returns whether this set contains another set or not
#pop()	                            Removes an element from the set
#remove()	                    Removes the specified element
#symmetric_difference()	            Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	    inserts the symmetric differences from this set and another
#union()	                            Return a set containing the union of sets
#update()	                    Update the set with the union of this set and others








