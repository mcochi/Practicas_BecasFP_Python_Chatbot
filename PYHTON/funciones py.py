#Creae una funcion
#En Python, una función se define usando la palabra clave def :

def my_function():
  print("Hello from a function")

#llamar a una funcion
#para llamar a una funcion, use el nombre de la funcion seguido de parentesis

def my_function():
  print("Hello from a function")

my_function()

#argumentos
#La información se puede pasar a funciones como argumentos.
#Los argumentos se especifican después del nombre de la función, entre paréntesis. Puede agregar tantos argumentos como desee, solo sepárelos con una coma.
#El siguiente ejemplo tiene una función con un argumento (fname). Cuando se llama a la función, pasamos un nombre, que se usa dentro de la función para imprimir el nombre completo:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#numero de argumentos
#De forma predeterminada, se debe llamar a una función con el número correcto de argumentos. Lo que significa que si su función espera 2 argumentos, debe llamar a la función con 2 argumentos, ni más ni menos.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Argumentos arbitrarios, * argumentos
#Si no sabe cuántos argumentos se pasarán a su función, agregue un *antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#argumentos de palabras clave
#tambien puede enviar argumentos con la sintaxis clave = valor.
#De esta manera, el orden de los argumentos no importa.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Argumentos de palabras clave arbitrarias, ** kwargs
#Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos: **antes del nombre del parámetro en la definición de la función.
#De esta forma, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Valor de parámetro predeterminado
#El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.
#Si llamamos a la función sin argumento, usa el valor predeterminado:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#pasar una lista como argumento
#Puede enviar cualquier tipo de datos de argumento a una función (cadena, número, lista, diccionario, etc.), y se tratará como el mismo tipo de datos dentro de la función.
#Por ejemplo, si envía una Lista como argumento, seguirá siendo una Lista cuando llegue a la función:

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#valores devueltos
#Para permitir que una función devuelva un valor, use la return declaración:

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#la declaracion del pase
#functionLas definiciones no pueden estar vacías, pero si por alguna razón tiene una functiondefinición sin contenido, colóquela en la passdeclaración para evitar errores.

def myfunction():
  pass

#Ejemplo de recursividad
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


