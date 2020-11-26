#Python para bucles
#Un bucle for se usa para iterar sobre una secuencia (que es una lista, una tupla, un diccionario, un conjunto o una cadena).
#Esto es menos parecido a la palabra clave for en otros lenguajes de programación y funciona más como un método iterador que se encuentra en otros lenguajes de programación orientados a objetos.
#Con el bucle for podemos ejecutar un conjunto de declaraciones, una vez para cada elemento de una lista, tupla, conjunto, etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#El bucle for no requiere que se establezca una variable de indexación de antemano.


#Bucle a través de una cuerda
#Incluso las cadenas son objetos iterables, contienen una secuencia de caracteres:

for x in "banana":
  print(x)
  

#La declaración de descanso
#Con la instrucción break podemos detener el ciclo antes de que haya pasado por todos los elementos

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

####

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#La declaración de continuar
#Con la instrucción continue podemos detener la iteración actual del ciclo y continuar con la siguiente:
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#La función range ()
#Para recorrer un conjunto de código un número específico de veces, podemos usar la función range () ,
#La función range () devuelve una secuencia de números, comenzando desde 0 de manera predeterminada, se incrementa en 1 (de manera predeterminada) y termina en un número especificado.

for x in range(6):
  print(x)
#Tenga en cuenta que el rango (6) no son los valores de 0 a 6, sino los valores de 0 a 5.

#La función range () tiene por defecto 0 como valor inicial, sin embargo, es posible especificar el valor inicial agregando un parámetro: range (2, 6) , que significa valores de 2 a 6 (pero sin incluir 6):
  
for x in range(2, 6):
  print(x)

#La función range () tiene como valor predeterminado incrementar la secuencia en 1, sin embargo, es posible especificar el valor de incremento agregando un tercer parámetro: range (2, 30, 3 ) :
  
for x in range(2, 30, 3):
  print(x)

#Más en For Loop
#La elsepalabra clave en un forbucle especifica un bloque de código que se ejecutará cuando finalice el bucle:
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Bucles anidados
#Un bucle anidado es un bucle dentro de un bucle.
#El "bucle interno" se ejecutará una vez por cada iteración del "bucle externo"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#La declaración del pase
#forLos bucles no pueden estar vacíos, pero si por alguna razón tiene un forbucle sin contenido, passingrese la declaración para evitar errores.
for x in [0, 1, 2]:
  pass
