#ALCANZE DE PYTHON

#Alcance local
#Una variable creada dentro de una función pertenece al ámbito local de esa función y solo se puede usar dentro de esa función.

def myfunc():
  x = 300
  print(x)

myfunc()

#Función dentro de la función
#Como se explicó en el ejemplo anterior, la variable xno está disponible fuera de la función, pero está disponible para cualquier función dentro de la función:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


#Alcance global
#Una variable creada en el cuerpo principal del código Python es una variable global y pertenece al ámbito global.
#Las variables globales están disponibles desde cualquier ámbito, global y local.

x = 300

def myfunc():
  print(x)

myfunc()

print(x)


#Nombrar variables
#Si opera con el mismo nombre de variable dentro y fuera de una función, Python las tratará como dos variables separadas, una disponible en el ámbito global (fuera de la función) y otra disponible en el ámbito local (dentro de la función):

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Palabra clave global
#Si necesita crear una variable global, pero está atascado en el ámbito local, puede usar la globalpalabra clave.
#La globalpalabra clave hace que la variable sea global.

def myfunc():
  global x
  x = 300

myfunc()

print(x)

#Además, use la globalpalabra clave si desea realizar un cambio en una variable global dentro de una función.

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
