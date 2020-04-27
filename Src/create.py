
#Importación de librerías
import datetime

#Importación de módulos
from Src.mongoThings import *
from Src.locate import *
from Src.errorHandling import *

#Función de creación de variables principales
def createVar(*creation, value=0, tipo="Hora_Pool", method = "variables"):
    vehicle = [element.capitalize() for element in creation[0].split(",")]
    print(vehicle)
    db = pickDB()
    selectID = locateID(method=method, tipo=tipo)

    if "Pool" in tipo:
        vehicleDefined = ["Ranchera", "Turismo", "Minibus", "Diafana"]
    elif "Disposicion" in tipo:
        vehicleDefined = ["Ranchera", "Turismo", "Minibus", "Diafana", "Diafanavest"]
    elif tipo =="Basico":
        vehicleDefined = ["Vale", "Exterior", "Extras"]
    elif tipo =="Km_extras":
        vehicleDefined = ["Turismo", "Minibus", "Diafana"]
    elif tipo =="Dieta":
        vehicleDefined = ["Completa", "Reducida"]

    for element in vehicle:
        if element in vehicleDefined:
            checkDuplicated = locateDuplicated(element, method=method,tipo=tipo)
            position = locateIndex(tipo, element, method=method)
            if checkDuplicated == True:
                db.update({"_id":selectID}, {"$set":{f"{tipo}.{position}.{element}":value}})
            elif checkDuplicated == False:
                db.update({"_id":selectID}, {"$addToSet":{f"{tipo}":{element:value}}})
        if element not in vehicleDefined:
            return f"No ha sido introducido: {element}"
    return "OK"

#Función introductora
def createIntro():
    date = dateIntro()
    return date






