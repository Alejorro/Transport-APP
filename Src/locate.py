#Módulos
from Src.mongoThings import *

#Función Localizadora (Devuelve un ID en todos los casos)
def locateThings(method="variables", tipo="Pool", search="id"):

    if method == "variables":
        try:
            db = pickDB()
            projection = {"id":1}
            limit = 1
            resultID = db.find(projection=projection, limit=limit)
            return resultID[0]["_id"]
        except IndexError:
            db = pickDB()
            db.insert_one({tipo:[]})
            projection = {"id":1}
            limit = 1
            resultID = db.find(projection=projection, limit=limit)
            return resultID[0]["_id"]

            


