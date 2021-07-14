from flask import Flask, jsonify
from ML.proyecto import geocoders
from conexion.conexion import getDirecciones
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# Get Data Routes
@app.route('/ml/<int:cluster>')
def getCluster(cluster):
    repartidores = getDirecciones()
    direcciones = []
    for ubi in getDirecciones():
        direccion = ubi['direccion']
        direcciones.append(direccion)
    lon = len(getDirecciones())
    data = geocoders(direcciones,cluster)
    if data:
        for k in range(lon):
            nums = []
            for i in data:
                num = int(i)
                nums.append(num)
            repartidores[k]['Repartidor'] = nums[k]
        return jsonify({'Repartidores': {
            'message': 'PEDIDOS DE HOY',
            'data': repartidores}})
    else:
        return jsonify({'Repartidores': {
            'message': 'NO HAY PEDIDOS POR HOY'}})


    



if __name__ == '__main__':
    app.run(debug=True)
