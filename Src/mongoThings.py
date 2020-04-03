
#Librerías
from pymongo import MongoClient

#Inicialización BBDD
client = MongoClient("mongodb://localhost:27017/TransportAPP")
db = client.get_database()

#Creación/Selección de colecciones
def pickDB(method="variables"):
    if method == "variables":
        return db["Variables"]
    else:
        return db["Cronología"]
