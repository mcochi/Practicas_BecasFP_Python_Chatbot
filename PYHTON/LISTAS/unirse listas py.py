#UNIR DOS LISTAS
#Hay varias formas de unir o concatenar dos o más listas en Python.
#Una de las formas más sencillas es utilizar el + operador.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Otra forma de unir dos listas es agregando todos los elementos de list2 a list1, uno por uno:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#O puede usar el extend() método, cuyo propósito es agregar elementos de una lista a otra lista:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
