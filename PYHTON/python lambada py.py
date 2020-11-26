#python lambda
#Una función lambda es una pequeña función anónima.
#Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión.

#Sintaxis
#lambda arguments : expression

x = lambda a : a + 10
print(x(5))


#Las funciones Lambda pueden tomar cualquier número de argumentos:
x = lambda a, b : a * b
print(x(5, 6))

#Resumir el argumento a, by cy devolver el resultado:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#¿Por qué utilizar las funciones Lambda?
#El poder de lambda se muestra mejor cuando los usa como una función anónima dentro de otra función.
#Supongamos que tiene una definición de función que toma un argumento, y ese argumento se multiplicará por un número desconocido:

def myfunc(n):
  return lambda a : a * n


#Usa esa definición de función para hacer una función que siempre duplique el número que envías:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#O use la misma definición de función para hacer una función que siempre triplique el número que envía:

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#O use la misma definición de función para hacer ambas funciones, en el mismo programa:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Utilice funciones lambda cuando se requiera una función anónima durante un período corto de tiempo.

