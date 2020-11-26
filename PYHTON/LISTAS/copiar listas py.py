#COPIAR UNA LISTA
#No se puede copiar una lista simplemente escribiendo list2 = list1, ya que: list2sólo será una referencia a list1,
#y los cambios realizados en list1Automáticamente, también sean por list2.
#Hay formas de hacer una copia, una forma es utilizar el método List integrado copy().

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Otra forma de hacer una copia es utilizar el método integrado list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
