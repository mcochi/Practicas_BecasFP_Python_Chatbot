#Formato de cadena de Python
#Formato de cadena ()
#El format()método le permite formatear partes seleccionadas de una cadena.
#A veces hay partes de un texto que no controlas, ¿tal vez provienen de una base de datos o de una entrada de usuario?
#Para controlar dichos valores, agregue marcadores de posición (corchetes {}) en el texto y ejecute los valores a través del format()método:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))


#Puede agregar parámetros dentro de las llaves para especificar cómo convertir el valor:
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

#Valores múltiples
#Si desea usar más valores, simplemente agregue más valores al método format ():

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#Números de índice
#Puede usar números de índice (un número dentro de las llaves {0}) para asegurarse de que los valores se coloquen en los marcadores de posición correctos:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#Índices nombrados
#También puede usar índices con nombre ingresando un nombre dentro de las llaves {carname}, pero luego debe usar nombres cuando pase los valores de los parámetros txt.format(carname = "Ford"):

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))


