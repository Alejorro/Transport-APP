
#Importación de módulos
from Src.mongoThings import *
from Src.locate import *

def createPool(*vehicle, value=0):
    vehicle = [element.capitalize() for element in vehicle[0].split(",")]
    db = pickDB()
    selectID = locateID()

    vehicleDefined = ["Ranchera", "Turismo", "Minibus", "Diafana"]

    for element in vehicle:
        if element in vehicleDefined:
            checkDuplicated = locateDuplicated(element, method="variables")

            if checkDuplicated == True:
                db.update({"_id":selectID}, {"$set":{"Pool":[{element:value}]}})
            elif checkDuplicated == False:
                db.update({"_id":selectID}, {"$addToSet":{"Pool":{element:value}}})

    return "OK"
