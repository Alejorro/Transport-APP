#Librerías
from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
import json

#Módulos
from Src.create import *

#Inicialización APP:
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/pool/hora/<vehicle>')
def hourPool(vehicle):
    value = request.args.get('value')
    output = createVar(vehicle, value=value)
    return dumps(output)

@app.route('/disp/hora/<vehicle>')
def hourDisp(vehicle):
    value = request.args.get('value')
    output = createVar(vehicle, value=value, tipo="Hora_Disposicion")
    return dumps(output)

@app.route('/var/<element>')
def varBasic(element):
    value = request.args.get('value')
    output = createVar(element, value=value, tipo="Basico")
    return dumps(output)

@app.route('/var/km/<vehicle>')
def kmVar(vehicle):
    value = request.args.get('value')
    output = createVar(vehicle, value=value, tipo="Km_extras")
    return dumps(output)

@app.route('/var/dieta/<element>')
def dietVar(element):
    value = request.args.get('value')
    output = createVar(element, vehicle, value=value, tipo="Dieta")
    return dumps(output)

@app.route('/pool/jorn/<vehicle>')
def poolJorn(vehicle):
    value = request.args.get('value')
    output = createVar(vehicle, value=value, tipo="Jornada_Pool")
    return dumps(output)

@app.route('/disp/jorn/<vehicle>')
def poolDisp(vehicle):
    value = request.args.get('value')
    output = createVar(vehicle, value=value, tipo="Jornada_Disposicion")
    return dumps(output)

@app.route('/intro')
def introDay():
    output = createIntro()





app.run("0.0.0.0", 4500, debug=True)