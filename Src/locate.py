#Módulos
from Src.mongoThings import *

#Función localizadora de ID (Devuelve un ID en todos los casos)
def locateID(method="variables"):

    if method=="variables":
        db = pickDB()

    try:
        projection = {"_id":1}
        limit = 1
        resultID = db.find(projection=projection, limit=limit)
        return resultID[0]["_id"]
    except IndexError:
        db = pickDB()
        db.insert_one({tipo:[]})
        projection = {"_id":1}
        limit = 1
        resultID = db.find(projection=projection, limit=limit)
        return resultID[0]["_id"]

#Función localizadora de duplicados 
def locateDuplicated(searching, method="variables",tipo="Pool"):

    if method == "variables":
        db = pickDB()

    filtered={f"{tipo}.{searching}":{"$gt":"0"}}
    projection={"_id":1}
    limit=1
    resultDup = db.find(filter=filtered,projection=projection,limit=limit)

    filtered=({tipo:{searching:None}})
    projection={"_id":1}
    limit=1
    resultDup2 = db.find(filter=filtered,projection=projection,limit=limit)

    if len(list(resultDup))!= 0 or len(list(resultDup2))!=0:
        result = True
        
    elif len(list(resultDup))== 0 or len(list(resultDup2))==0:
        result = False

    return result