#Iteradores de Python
#Iterador vs Iterable
#Las listas, tuplas, diccionarios y conjuntos son todos objetos iterables. Son contenedores iterables de los que puede obtener un iterador.
#Todos estos objetos tienen un iter()método que se usa para obtener un iterador:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Incluso las cadenas son objetos iterables y pueden devolver un iterador:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Bucle a través de un iterador
#También podemos usar un forbucle para iterar a través de un objeto iterable:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#Itere los caracteres de una cadena:

mystr = "banana"

for x in mystr:
  print(x)


#Crea un iterador

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#StopIteration

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
