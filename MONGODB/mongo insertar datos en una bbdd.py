import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "Marcos", "address": "Sevilla", "apellido": "Cochi" }
#se puede crear el campo apellido
x = mycol.insert_one(mydict)
