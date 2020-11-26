#FECHAS PYTHON
#Una fecha en Python no es un tipo de datos en sí misma, pero podemos importar un módulo con nombre datetimepara trabajar con fechas como objetos de fecha.

import datetime

x = datetime.datetime.now()
print(x)


#Salida de fecha

#Cuando ejecutamos el código del ejemplo anterior, el resultado será:

#2020-11-19 12:04:24.988428
#La fecha contiene año, mes, día, hora, minuto, segundo y microsegundo.

#El datetimemódulo tiene muchos métodos para devolver información sobre el objeto de fecha.

#Aquí hay algunos ejemplos, aprenderá más sobre ellos más adelante en este capítulo:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


#Crear objetos de fecha
#Para crear una fecha, podemos usar la datetime()clase (constructor) del datetimemódulo.
#La datetime()clase requiere tres parámetros para crear una fecha: año, mes, día.

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
#La datetime()clase también toma parámetros para la hora y la zona horaria (hora, minuto, segundo, microsegundo, tzone), pero son opcionales y tiene un valor predeterminado de 0, ( Nonepara la zona horaria).

#El método strftime ()
#El datetimeobjeto tiene un método para formatear objetos de fecha en cadenas legibles.
#Se llama al método strftime(), y toma un parámetro format, para especificar el formato de la cadena devuelta:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


#Directive	Description	    Example	
#%a	Weekday, short version	    Wed	
#%A	Weekday, full version	    Wednesday	
#%w	Weekday as a number 0-6, 0 is Sunday	3	
#%d	Day of month 01-31	31	
#%b	Month name, short version	Dec	
#%B	Month name, full version	December	
#%m	Month as a number 01-12	12	
#%y	Year, short version, without century	18	
#%Y	Year, full version	2018	
#%H	Hour 00-23	17	
#%I	Hour 00-12	05	
#%p	AM/PM	PM	
#%M	Minute 00-59	41	
#%S	Second 00-59	08	
#%f	Microsecond 000000-999999	548513	
#%z	UTC offset	+0100	
#%Z	Timezone	CST	
#%j	Day number of year 001-366	365	
#%U	Week number of year, Sunday as the first day of week, 00-53	52	
#%W	Week number of year, Monday as the first day of week, 00-53	52	
#%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
#%x	Local version of date	12/31/18	
#%X	Local version of time	17:41:00	
#%%	A % character	%

    
