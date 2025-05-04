import pandas as pd
import psycopg2
import os

# Configuración de conexión a PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    dbname="english_app",
    user="antonio",           # Cambia esto si usas otro nombre
    password="?Terremoto22"               # Si creaste el usuario sin contraseña, deja vacío
)
cursor = conn.cursor()

# Crear tabla (solo una vez)
cursor.execute("""
    DROP TABLE IF EXISTS palabras;
    CREATE TABLE palabras (
        id SERIAL PRIMARY KEY,
        categoria TEXT,
        ingles TEXT,
        pronunciacion TEXT,
        traduccion TEXT,
        visualizacion TEXT DEFAULT NULL
    );
""")
conn.commit()

# Lista de archivos CSV
archivos_csv = [
    'data/csv/especif_words.csv',
    'data/csv/nom_adj.csv',
    'data/csv/other_words.csv',
    'data/csv/verbs.csv'
]

# Importar datos de cada archivo
for archivo in archivos_csv:
    if not os.path.exists(archivo):
        print(f"No se encontró el archivo {archivo}. Saltando...")
        continue

    df = pd.read_csv(archivo, header=None, names=["Categoria", "Ingles", "Pronunciacion", "Traduccion", "ID"])

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO palabras (categoria, ingles, pronunciacion, traduccion)
            VALUES (%s, %s, %s, %s)
        """, (row["Categoria"], row["Ingles"], row["Pronunciacion"], row["Traduccion"]))

    print(f"Importado: {archivo}")

conn.commit()
cursor.close()
conn.close()
print("✅ Todos los datos han sido importados correctamente.")
