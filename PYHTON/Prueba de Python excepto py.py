#Prueba de Python excepto
#El trybloque le permite probar un bloque de código en busca de errores.
#El exceptbloque le permite manejar el error.
#El finallybloque le permite ejecutar código, independientemente del resultado de los bloques try y except.

#Manejo de excepciones

#The try block will generate an error, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

#Muchas excepciones

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#Más

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#Finalmente

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")




  
