#HERENCIA DE PYTHON
#Crear una clase para padres
#Cualquier clase puede ser una clase principal, por lo que la sintaxis es la misma que la de crear cualquier otra clase:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#Crear una clase secundaria
#Para crear una clase que herede la funcionalidad de otra clase, envíe la clase principal como parámetro al crear la clase secundaria:
#Cree una clase llamada Student, que heredará las propiedades y métodos de la Personclase:

class Student(Person):
  pass
#Nota: Utilice la pass palabra clave cuando no desee agregar otras propiedades o métodos a la clase.

#Ahora la clase Student tiene las mismas propiedades y métodos que la clase Person.

x = Student("Mike", "Olsen")
x.printname()

#Utilice la función super ()
#Python también tiene una super()función que hará que la clase hija herede todos los métodos y propiedades de su padre:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#Agregar propiedades

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

#En el siguiente ejemplo, el año 2019debería ser una variable y pasar a la Studentclase al crear objetos para estudiantes. Para hacerlo, agregue otro parámetro en la función __init __ ():

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

#Agregar métodos
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

