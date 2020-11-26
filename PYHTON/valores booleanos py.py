#VALORES BOOLEANOS
#En programación, a menudo necesita saber si una expresión es Trueo False.
#Puede evaluar cualquier expresión en Python y obtener una de dos respuestas, Trueo False.
#Cuando compara dos valores, la expresión se evalúa y Python devuelve la respuesta booleana

print(10 > 9)
print(10 == 9)
print(10 < 9)
print(5 == 5)


#Cuando ejecuta una condición en una declaración if, Python devuelve Trueo False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#EVALUAR VALORES Y VARIABLES

#La bool()función te permite evaluar cualquier valor y darte Trueo False a cambio

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


#LA MAYORIADE VALORES SON VERDADEROS
#Casi cualquier valor se evalúa para determinar Truesi tiene algún tipo de contenido
#Cualquier cadena lo es True, excepto las cadenas vacías
#Cualquier número es True, excepto 0
#Cualquier lista, tupla, conjunto y diccionario son True, excepto los vacíos

print(bool("abc"))
print(bool(123))                            #todos true 
print(bool(["apple", "cherry", "banana"]))



print(bool(False))
print(bool(None))
print(bool(0))                       
print(bool(""))             #todos false
print(bool(()))
print(bool([]))
print(bool({}))


#Un valor más, u objeto en este caso, se evalúa False, y eso es si tiene un objeto que
#está hecho de una clase con una __len__función que devuelve 0o False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#Las funciones pueden devolver un booleano

def myFunction() :
  return True

print(myFunction())

#Puede ejecutar código basado en la respuesta booleana de una función

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


#Python también tiene muchas funciones integradas que devuelven un valor booleano,
#como la isinstance() función, que se puede usar para determinar si un objeto es de un determinado tipo de datos

x = 200                   #comprueba si es un numero entero
print(isinstance(x, int))
