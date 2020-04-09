
#Importación de módulos
from Src.mongoThings import *
from Src.locate import *

def createVar(*vehicle, value=0, tipo="Pool"):
    vehicle = [element.capitalize() for element in vehicle[0].split(",")]
    db = pickDB()
    selectID = locateID()

    vehicleDefined = ["Ranchera", "Turismo", "Minibus", "Diafana"]

    for element in vehicle:

        print(vehicle)
        if element in vehicleDefined:
            checkDuplicated = locateDuplicated(element, method="variables",tipo=tipo)

            if checkDuplicated == True:
                db.update({"_id":selectID}, {"$set":{f"{tipo}":[{element:value}]}})
            elif checkDuplicated == False:
                db.update({"_id":selectID}, {"$addToSet":{f"{tipo}":{element:value}}})

    return "OK"
