#CAMBIAR EL VALOR DE UN ARTIULO
#Para cambiar el valor de un artículo específico, consulte el número de índice:
#Cambie el segundo elemento:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Para insertar más de un elemento, cree una lista con los nuevos valores y especifique el número
#de índice donde desea que se inserten los nuevos valores:
#Cambie el segundo valor reemplazándolo con dos nuevos valores:


thislist = ["apple", "banana", "cherry"]
thislist[1] = ["blackcurrant", "watermelon"]
print(thislist)
#Nota: La longitud de la lista cambiará cuando el número de elementos insertados no coincida con el número de elementos reemplazados.


#CAMBIAR UN RANGODE VALORES DE ARTICULO
#Para cambiar el valor de los elementos dentro de un rango específico, defina una lista con los nuevos valores y consulte el rango de
#números de índice donde desea insertar los nuevos valores:

#Cambie los valores "plátano" y "cereza" por los valores "grosella negra" y "sandía":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#INSERTAR ELEMNTOS
#Para insertar un nuevo elemento de lista, sin reemplazar ninguno de los valores existentes, podemos usar el insert()método.
#El insert()método inserta un elemento en el índice especificado:
#Inserte "sandía" como tercer elemento:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#Nota: Como resultado del ejemplo anterior, la lista ahora contendrá 4 elementos.
