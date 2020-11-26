#Hay tres tipos numéricos en Python:

#int
#float
#complex

x = 1       #int
y = 2.8     #float
z = 1J      #complex

print(type(x))
print(type(y))
print(type(z))


#INT
#Int, o entero, es un número entero, positivo o negativo,
#sin decimales, de longitud ilimitada.

x = 1
y = 357645763485766
z = -5151518548
print(type(x))
print(type(y))
print(type(z))

#FLOAT
#Float, o "número de coma flotante" es un número, positivo o negativo,
#que contiene uno o más decimales.

x = 1.10
y = 1.0
z = -35.5987
print(type(x))
print(type(y))
print(type(z))

#Float también pueden ser números científicos con una "e"
#para indicar la potencia de 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


#COMPLEX
#Los números complejos se escriben con una "j" como parte imaginaria:

x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))


#CONVERSION DE UN TIPO A OTRO
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#NUMERO ALEATORIO
#Importe el módulo aleatorio y muestre un número aleatorio entre 1 y 9:

import random

print(random.randrange(1, 10))

