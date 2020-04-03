
#Importación de módulos
from Src.mongoThings import *
from Src.locate import *

def createPool(*vehicle, db=0, value=0):
    vehicle = vehicle[0].split(",")
    db = pickDB()
    selectID = locateThings()
    if "ranchera" in vehicle:
        db.update({"_id":selectID}, {"$set":{"Pool":{"Ranchera":value}}})
        db.update({"_id":selectID}, {"$addToSet":{"Pool":{"Ranchera":value}}})
    if "turismo" in vehicle:
        db.update({"_id":selectID}, {"$push":{"Pool":{"Turismo":value}}})
    if "minibus" in vehicle:
        db.update({"_id":selectID}, {"$set":{"Minibus-Ruta":value}})
    if "diafana" in vehicle:
        db.update({"_id":selectID}, {"$set":{"Diáfana":value}})
    return "OK"

def createPrincipales(*apartados, db=0, value=0):
    apartados = apartados[0].split(",")
    db = pickDB()
    selectID = locateThings()
    if "vales" in apartados:
        db.update({"_id":selectID[0]["_id"]}, {"$set":{"Vales":value}})
    if "exterior" in apartados:
        db.update({"_id":selectID[0]["_id"]}, {"$set":{"Comida Exterior":value}})
    if "horas" in apartados:
        db.update({"_id":selectID[0]["_id"]}, {"$set":{"Horas Extras":value}})
    if "dietacomp" in apartados:
        db.update({"_id":selectID[0]["_id"]}, {"$set":{"Dieta Completa":value}})
    if "dietared" in apartados:
        db.update({"_id":selectID[0]["_id"]}, {"$set":{"Dieta Reducida":value}})    
    if "turismoskm" in apartados:
        db.update({"_id":selectID[0]["_id"]}, {"$set":{"Turismos Km Extras":value}})
    if "minibuskm" in apartados:
        db.update({"_id":selectID[0]["_id"]}, {"$set":{"Minibus Km Extras":value}})
    return "OK"






    



