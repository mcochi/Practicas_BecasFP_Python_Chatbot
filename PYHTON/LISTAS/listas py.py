#LISTA
#Las listas se utilizan para almacenar varios elementos en una sola variable.
#Las listas son uno de los 4 tipos de datos integrados en Python que se utilizan
#para almacenar colecciones de datos, los otros 3 son Tuple , Set y Dictionary , todos con diferentes calidades y usos.
#Las listas se crean utilizando corchetes

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Las listas, puden tener elementos con el mismo valor.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Longitud de lista
#Para determinar cuántos elementos tiene una lista, use la len()función:

thislist = ["apple", "banana", "cherry","jamon"]
print(len(thislist))

#Elementos de lista: tipos de datos
#Los elementos de la lista pueden ser de cualquier tipo de datos:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#Una lista puede contener diferentes tipos de datos:

list1 = ["abc", 34, True, 40, "male"]
print(list1)


#Desde la perspectiva de Python, las listas se definen como objetos con el tipo de datos 'lista':

#<class 'list'>

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


#El constructor list ()
#También es posible utilizar el constructor list () al crear una nueva lista.

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


