#Entrada de usuario de Python
#Entrada del usuario
#Python permite la entrada del usuario.
#Eso significa que podemos pedirle información al usuario.
#El método es un poco diferente en Python 3.6 que en Python 2.7.
#Python 3.6 usa el input()método.
#Python 2.7 usa el raw_input()método.
#El siguiente ejemplo solicita el nombre de usuario, y cuando ingresó el nombre de usuario, se imprime en la pantalla:

username = input("Enter username:")
print("Username is: " + username)


username = raw_input("Enter username:")
print("Username is: " + username)
#Python deja de ejecutarse cuando se trata de la input()función y continúa cuando el usuario ha dado alguna entrada.
