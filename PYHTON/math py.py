#python math 

#Funciones matemáticas integradas
#Las funciones min()y max()se pueden usar para encontrar el valor más bajo o más alto en un iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


#La abs()función devuelve el valor absoluto (positivo) del número especificado:

x = abs(-7.25)

print(x)

#La función devuelve el valor de x elevado a la potencia de y (x y ).pow(x, y)

x = pow(4, 3)

print(x)

#El módulo de matemáticas
#Python también tiene un módulo incorporado llamado math, que extiende la lista de funciones matemáticas.
#Para usarlo, debe importar el mathmódulo:
#import math
#Cuando haya importado el mathmódulo, puede comenzar a usar métodos y constantes del módulo.

#El math.sqrt()método, por ejemplo, devuelve la raíz cuadrada de un número:

import math

x = math.sqrt(64)

print(x)

#El math.ceil()método redondea un número hacia arriba a su entero más cercano, y el math.floor() método redondea un número hacia abajo a su entero más cercano y devuelve el resultado:

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#La math.piconstante, devuelve el valor de PI (3,14 ...):

import math

x = math.pi

print(x)


