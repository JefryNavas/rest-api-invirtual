import psycopg2
from datetime import date

#Día actual
today = date.today()
conexion1 = psycopg2.connect(
    host="invirtualdb.postgres.database.azure.com",
    dbname="invirtual",
    user="invirtualadmin@invirtualdb",
    password="2303Titulacion",
    port = '5432',
    sslmode='require')
cursor = conexion1.cursor()

def getDirecciones():
    direcciones = []
    cursor.execute(
        f"SELECT cod_ped,calle_principal from pedido where fecha_entrega = '{today}'" +
        " and estado = 'Pedido Registrado'"
    )
    col = []
    for calle in cursor.fetchall():
        cal = list(calle)
        if not cal == col:
            direcciones.append({'cod_pedido': cal[0],'direccion': f'{cal[1]}, Quito'}) 
        col = cal
    return direcciones

