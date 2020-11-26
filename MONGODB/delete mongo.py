#Nota: Si la consulta encuentra más de un documento, solo se elimina la primera aparición.


#Borre el documento con la dirección "Logroño":
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Logroño" }

mycol.delete_one(myquery)




#Eliminar mas de un documento
#Para eliminar más de un documento, use el delete_many()método.
#El primer parámetro del delete_many()método es un objeto de consulta que define qué documentos eliminar.


#Elimine todos los documentos donde la dirección comience con la letra S:
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": {"$regex": "^L"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")
