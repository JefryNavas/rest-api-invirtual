
from flask import Flask, jsonify, request
import numpy as np
import json
from ML.proyecto import geocoders
from conexion.conexion import direcciones
app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False

#DATA

# Get Data Routes
@app.route('/ml/<int:cluster>')
def getCluster(cluster):
    repartidores = []
    for i in geocoders(direcciones,cluster):
        num = int(i)
        repartidores.append({'Dirección': num})
    return jsonify({'Repartidores': repartidores})



if __name__ == '__main__':
    app.run(debug=True)
