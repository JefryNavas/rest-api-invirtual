import psycopg2
from datetime import date
from datetime import datetime
#Día actual
today = date.today()

conexion1 = psycopg2.connect(host="localhost",database="Invirtual_Store",user="postgres",password="123")

direcciones = []

# Conexion con la base en Postgres
cursor = conexion1.cursor()

# Consulta las palabras kichwa con etiquetas positivas
cursor.execute(
    f"SELECT calle_principal from pedido"
)
for calle in cursor.fetchall():
    cal = "".join(calle)
    if not cal in direcciones:
        direcciones.append(f'{cal}')


print(direcciones)