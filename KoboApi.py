import requests
import psycopg2
import pandas as pd


'''
# Credenciales y URL de KoboToolbox
KOBO_URL = 'https://kf.kobotoolbox.org/api/v2/assets/{asset_uid}/data/'
USERNAME = 'Monstersle'
PASSWORD = 'tu_contraseña'
ASSET_UID = 'id_de_la_encuesta'

# Conexión a PostgreSQL
conn = psycopg2.connect(
    dbname="nombre_bd",
    user="usuario_bd",
    password="password_bd",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Obtener los datos de KoboToolbox en formato JSON
response = requests.get(KOBO_URL.format(asset_uid=ASSET_UID), auth=(USERNAME, PASSWORD))
data = response.json()

# Convertir los datos JSON en un DataFrame de Pandas
df = pd.json_normalize(data['results'])

# Crear la tabla en PostgreSQL (si no existe)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS encuestas (
        id SERIAL PRIMARY KEY,
        campo1 TEXT,
        campo2 TEXT,
        campo3 TEXT
        -- Agrega las columnas necesarias según tu encuesta
    )
""")

# Insertar los datos en la base de datos
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO encuestas (campo1, campo2, campo3) 
        VALUES (%s, %s, %s)
    """, (row['campo1'], row['campo2'], row['campo3']))

# Guardar cambios y cerrar conexión
conn.commit()
cursor.close()
conn.close()

'''