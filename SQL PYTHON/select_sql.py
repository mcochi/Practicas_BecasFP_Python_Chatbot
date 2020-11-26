import mysql.connector

# Me conecto
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  port="33060"
)

print(mydb)

# A mi conexión le incluyo un curso que gestiona la i/o a la BBDD
mycursor = mydb.cursor()

sql = ("SELECT * FROM demo.prueba_coda")

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
