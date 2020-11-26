#Diccionario
#Un diccionario es una colección desordenada, modificable e indexada. En Python, los diccionarios se escriben con llaves y tienen claves y valores.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Acceder a elementos
#Puede acceder a los elementos de un diccionario haciendo referencia a su nombre clave, entre corchetes:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#También hay un método llamado get()que te dará el mismo resultado:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)


#Cambiar valores
#Puede cambiar el valor de un elemento específico consultando su nombre de clave:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#Recorrer un diccionario
#Puede recorrer un diccionario utilizando un forbucle.
#Al recorrer un diccionario, el valor de retorno son las claves del diccionario, pero también existen métodos para devolver los valores .

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#Imprima todos los valores en el diccionario, uno por uno:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

#También puede usar el values()método para devolver valores de un diccionario:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

#Recorra tanto las claves como los valores , utilizando el items()método:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

#Compruebe si la clave existe
#Para determinar si una clave específica está presente en un diccionario, use la inpalabra clave:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#LONGUITUD DEL DICCIONARIO
#Para determinar cuántos elementos (pares clave-valor) tiene un diccionario, use la len() función.

print(len(thisdict))

#Agregar elementos
#La adición de un elemento al diccionario se realiza utilizando una nueva clave de índice y asignándole un valor:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Eliminar elementos
#Existen varios métodos para eliminar elementos de un diccionario:

#El pop()método elimina el elemento con el nombre de clave especificado:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#El popitem()método elimina el último elemento insertado (en las versiones anteriores a la 3.7, se elimina un elemento aleatorio):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#La delpalabra clave elimina el elemento con el nombre de clave especificado:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#El clear()método vacía el diccionario:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


#Copiar un diccionario
#No se puede copiar un diccionario simplemente escribiendo dict2 = dict1, ya que: dict2sólo será una referencia a dict1, y los cambios realizados en dict1Automáticamente, también sean por dict2.
#Hay formas de hacer una copia, una forma es utilizar el método de diccionario integrado copy().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Diccionarios anidados
#Un diccionario también puede contener muchos diccionarios, esto se denomina diccionarios anidados

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

#################

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)


#El constructor dict ()
#También es posible usar el constructor dict () para crear un nuevo diccionario:

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

