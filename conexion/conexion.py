import psycopg2
from datetime import date
from datetime import datetime
#Día actual
today = date.today()

conexion1 = psycopg2.connect(host="localhost",database="Invirtual_Store",user="postgres",password="123")
cursor = conexion1.cursor()

def getDirecciones():
    direcciones = []
    cursor.execute(
        f"SELECT cod_ped,calle_principal from pedido where fecha_entrega = '{today}' and estado = 'Pedido Registrado'"
    )
    col = []
    for calle in cursor.fetchall():
        cal = list(calle)
        if not cal == col:
            direcciones.append({'cod_pedido': cal[0],'direccion': f'{cal[1]}, Quito'}) 
        col = cal
    return direcciones

