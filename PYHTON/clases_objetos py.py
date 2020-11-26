#Crear una clase
#Para crear una clase, use la palabra clave class:

class MyClass:
  x = 5

print(MyClass)

#Crear objeto
#Ahora podemos usar la clase llamada MyClass para crear objetos:

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


#La función __init __ ()
#Los ejemplos anteriores son clases y objetos en su forma más simple y no son realmente útiles en aplicaciones de la vida real.
#Para entender el significado de las clases tenemos que entender la función incorporada __init __ ().
#Todas las clases tienen una función llamada __init __ (), que siempre se ejecuta cuando se inicia la clase.
#Utilice la función __init __ () para asignar valores a las propiedades del objeto u otras operaciones que sean necesarias para realizar cuando se crea el objeto:
 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#Nota: La __init__()función se llama automáticamente cada vez que se usa la clase para crear un nuevo objeto.

#Métodos de objetos
#Los objetos también pueden contener métodos. Los métodos en los objetos son funciones que pertenecen al objeto.
#Creemos un método en la clase Person:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#Nota: El selfparámetro es una referencia a la instancia actual de la clase y se usa para acceder a las variables que pertenecen a la clase.

#El auto parámetro
#El selfparámetro es una referencia a la instancia actual de la clase y se usa para acceder a las variables que pertenecen a la clase.
#No tiene que ser nombrado self, puedes llamarlo como quieras, pero tiene que ser el primer parámetro de cualquier función en la clase:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modificar las propiedades del objeto
#Puede modificar propiedades en objetos como este:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)

#La declaración del pase
#classLas definiciones no pueden estar vacías, pero si por alguna razón tiene una classdefinición sin contenido, colóquela en la passdeclaración para evitar errores.

class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement





