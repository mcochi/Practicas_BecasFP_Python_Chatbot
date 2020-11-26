#Condiciones de Python y declaraciones If
#Python admite las condiciones lógicas habituales de las matemáticas:

#Es igual a: a == b
#No es igual a: a! = B
#Menor que: a <b
#Menor o igual a: a <= b
#Mayor que: a> b
#Mayor o igual a: a> = b

#Estas condiciones se pueden utilizar de varias formas, más comúnmente en "sentencias if" y bucles.
#Una "instrucción if" se escribe utilizando la palabra clave if .

a = 33
b = 200
if b > a:
  print("b is greater than a")

#Elif
#La palabra clave elif es la forma que tiene Python de decir "si las condiciones anteriores no eran verdaderas, pruebe esta condición".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#Más
#La palabra clave else captura cualquier cosa que no sea detectada por las condiciones anteriores.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#####

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Mano corta si
#Si solo tiene una instrucción para ejecutar, puede ponerla en la misma línea que la instrucción if.

if a > b: print("a is greater than b")


#Mano corta Si ... Else
#a = 2
b = 330
print("A") if a > b else print("B")
#Esta técnica se conoce como Operadores ternarios o Expresiones condicionales .

######
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Y
#La palabra clave y es un operador lógico y se usa para combinar declaraciones condicionales:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


#O
#La orpalabra clave es un operador lógico y se usa para combinar declaraciones condicionales:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")    


#Anidado si
#Puede tener ifdeclaraciones dentro de ifdeclaraciones, esto se llama declaraciones anidadas if .

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#La declaración del pase
#ifLas declaraciones no pueden estar vacías, pero si por alguna razón tiene una ifdeclaración sin contenido, passintrodúzcala para evitar errores.

a = 33
b = 200

if b > a:
  pass



