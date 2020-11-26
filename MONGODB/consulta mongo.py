#Busque documento (s) con la dirección "Logroño"
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Logroño", "name": "Marcos"}

mydoc = mycol.find(myquery)
print("empiezo fase 1")
for x in mydoc:
  print(x)


#Busque documentos donde la dirección comience con la letra "L" o superior:
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$gt": "L" } }

mydoc = mycol.find(myquery)
print("empiezo fase 2")
for x in mydoc:
  print(x)




#Busque documentos donde la dirección comience con la letra "H":
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^H" } }

mydoc = mycol.find(myquery)
print("empiezo fase 3")
for x in mydoc:
  print(x)
