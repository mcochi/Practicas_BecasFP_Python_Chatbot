#Asignar cadena a una variable

a = "hElLo"
print(a)

#Cuerdas multilinea,
# puede asignar una cadena de variass lineas a una variable
#utilizando 3 comillas, o tres comillas simples

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#Como muchos otros lenguajes de programación populares, las
#cadenas en Python son matrices de bytes que representan caracteres Unicode.
#Sin embargo, Python no tiene un tipo de datos de carácter, un solo carácter
#es simplemente una cadena con una longitud de 1.
#Se pueden usar corchetes para acceder a elementos de la cadena.

a = "Hello, World!"
print(a[1])   #Obtenga el carácter en la posición 1 (recuerde que el primer carácter tiene la posición 0)
#cadewnas en python empiezan por el 0
#RABANAR
#Puede devolver un rango de caracteres utilizando la sintaxis de sector.
#Especifique el índice inicial y el índice final, separados por dos puntos,
#para devolver una parte de la cadena.

b = "Hello, World!"
print(b[2:5])   #Obtenga los personajes de la posición 2 a la posición 5 (no incluidos)


#INDEXACION MEGATIVA
#Use índices negativos para comenzar el segmento desde el final de la cadena

b = "Hello, World!" #Obtenga los caracteres de la posición 5 a la posición 1 (no incluido), comenzando el conteo desde el final de la cadena:
print(b[-5:-2])


#LONGITUD DE LA CUERDA
#La len()función devuelve la longitud de una cadena:

a = "Hello, World!"
print(len(a))

#METODOS DE CADENA
#El strip()método elimina cualquier espacio en blanco del principio o del final:

a = " Hello, World!         "
print(a.strip()) # returns "Hello, World!"

#El lower()método devuelve la cadena en minúsculas

a = "HellOO, WorlDD!"
print(a.lower())

#El upper()método devuelve la cadena en mayúsculas

a = "hello, World!"
print(a.upper())

#El replace()método reemplaza una cadena con otra cadena

a = "Hello, World!"
print(a.replace("H", "JJJJ"))

#El split()método divide la cadena en subcadenas si encuentra instancias del separador:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#COMPROBAR CADENA
#Compruebe si la frase "ain" está presente en el siguiente texto

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt                                   #true
print(x)

txt = "The ran in Span stays manly in the plan"
x = "ain" in txt                                    #false
print(x)

#Compruebe si la frase "ain" NO está presente en el siguiente texto

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)



#CONCATENACION DE CADENAS
#Fusionar variable acon variable ben variable c

a = "Hello"
b = "World"
c = a + b
print(c)

#Para agregar un espacio entre ellos, agregue un " "

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Utilice el format()método para insertar números en cadenas

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#El método format () toma un número ilimitado de argumentos y
#se colocan en los respectivos marcadores de posición

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Puede utilizar números de índice {0}para asegurarse de que los
#argumentos se coloquen en los marcadores de posición correctos

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#PERSONAJE DE ESCAPE
#n ejemplo de un carácter ilegal es una comilla doble dentro de una
#cadena que está rodeada por comillas dobles

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
