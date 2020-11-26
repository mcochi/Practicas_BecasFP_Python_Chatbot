#Bucles while de Python

#while loops
#for loops

#El bucle while
#Con el tiempo bucle podemos ejecutar un conjunto de instrucciones, siempre y cuando se cumpla una condición.

i = 1
while i < 6:
  print(i)
  i += 1
#Nota: recuerde incrementar i, de lo contrario el ciclo continuará para siempre.
#El tiempo de bucle requiere variables relevantes para estar listo, en este ejemplo, tenemos que definir una variable de indexación, i , lo que nos pone a 1.

#La declaración de descanso
#Con la sentencia break podemos detener el ciclo incluso si la condición while es verdadera:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


#La declaración de continuar
#Con la declaración continue podemos detener la iteración actual y continuar con la siguiente:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#La declaración else
#Con la instrucción else podemos ejecutar un bloque de código una vez cuando la condición ya no es verdadera:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



