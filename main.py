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

@app.route('/pool/<vehicle>')
def pool(vehicle):
    value = request.args.get('value')
    output = createPool(vehicle, value=value)
    return dumps(output)

@app.route('/principales/<apartados>')
def variables(apartados):
    value = request.args.get('value')
    output = createPool(apartados, value=value)
    return dumps(output)

app.run("0.0.0.0", 4500, debug=True)