#python RegEx

#Módulo RegEx
#Python tiene un paquete integrado llamado re, que se puede usar para trabajar con expresiones regulares.
#Importar el remódulo:

import re


#RegEx en Python
#Cuando haya importado el remódulo, puede comenzar a usar expresiones regulares:

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


#La función findall ()
#La findall()función devuelve una lista que contiene todas las coincidencias.

import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#La lista contiene las coincidencias en el orden en que se encuentran.
#Si no se encuentran coincidencias, se devuelve una lista vacía:

import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#La función search ()
#La search()función busca en la cadena una coincidencia y devuelve un objeto Match si hay una coincidencia.
#Si hay más de una coincidencia, solo se devolverá la primera aparición de la coincidencia:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Si no se encuentran coincidencias, Nonese devuelve el valor :
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#La función split ()
#La split()función devuelve una lista donde la cadena se ha dividido en cada coincidencia:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Puede controlar el número de ocurrencias especificando el maxsplit parámetro:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#La función sub ()
#La sub()función reemplaza las coincidencias con el texto de su elección:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Puede controlar el número de reemplazos especificando el count parámetro:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#Coincidir con objeto
#Nota: Si no hay coincidencia, Nonese devolverá el valor , en lugar del objeto de coincidencia.

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object




import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())



import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
    


  
