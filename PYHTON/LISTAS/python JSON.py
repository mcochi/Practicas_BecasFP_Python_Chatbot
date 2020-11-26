#python JSON

#Python tiene un paquete incorporado llamado json, que se puede usar para trabajar con datos JSON.

import json

#Parse JSON - Convertir de JSON a Python
#Si tiene una cadena JSON, puede analizarla utilizando el json.loads()método.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#Convertir de Python a JSON
#Si tiene un objeto Python, puede convertirlo en una cadena JSON utilizando el json.dumps()método.

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


#Puede convertir objetos de Python de los siguientes tipos en cadenas JSON:

#dictar
#lista
#tupla
#cuerda
#En t
#flotador
#Cierto
#Falso
#Ninguna

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Convierta un objeto Python que contenga todos los tipos de datos legales

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


#Dar formato al resultado
#El ejemplo anterior imprime una cadena JSON, pero no es muy fácil de leer, sin sangrías ni saltos de línea.
#El json.dumps()método tiene parámetros para facilitar la lectura del resultado:

json.dumps(x, indent=4)

#También puede definir los separadores, el valor predeterminado es (",", ":"), lo que significa usar una coma y un espacio para separar cada objeto, y dos puntos y un espacio para separar las claves de los valores:

json.dumps(x, indent=4, separators=(". ", " = "))

#Ordenar el resultado
#El json.dumps()método tiene parámetros para ordenar las claves en el resultado:
#Utilice el sort_keysparámetro para especificar si el resultado debe ordenarse o no:

json.dumps(x, indent=4, sort_keys=True)



  





