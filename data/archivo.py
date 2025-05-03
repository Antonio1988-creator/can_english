import pandas as pd
import re
import os

def procesar_csv_a_excel_por_hojas(archivo_csv, archivo_excel):
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv, header=None, names=["Categoría", "Inglés", "Pronunciación", "Traducción"])
    
    # Crear un diccionario para agrupar las filas por la primera columna (Categoría)
    hojas = {}
    for categoria, grupo in df.groupby("Categoría"):
        # Crear un DataFrame para cada categoría con las columnas requeridas
        hoja = grupo[["Inglés", "Pronunciación", "Traducción"]].copy()
        hoja["Visualización"] = ""  # Añadir la columna vacía
        # Limpiar el nombre de la hoja eliminando caracteres no válidos
        nombre_hoja = re.sub(r'[\\/*?:\[\]]', '', categoria)[:31]  # Limitar a 31 caracteres
        hojas[nombre_hoja] = hoja

    # Escribir las hojas en un archivo Excel
    with pd.ExcelWriter(archivo_excel, engine="openpyxl") as writer:
        for nombre_hoja, contenido in hojas.items():
            contenido.to_excel(writer, sheet_name=nombre_hoja, index=False)

# Lista de tus archivos CSV y los nombres para los archivos Excel de salida
archivos_csv = ['nom_adj.csv', 'otras.csv', 'programac.csv', 'verbos.csv']
archivos_excel = ['nom_adj.xlsx', 'otras.xlsx', 'programac.xlsx', 'verbos.xlsx']

# Procesar cada archivo CSV y generar su respectivo archivo Excel
for archivo_csv, archivo_excel in zip(archivos_csv, archivos_excel):
    if not os.path.exists(archivo_csv):
        print(f"El archivo {archivo_csv} no se encontró. Saltando...")
        continue
    try:
        procesar_csv_a_excel_por_hojas(archivo_csv, archivo_excel)
        print(f"Se ha generado el archivo: {archivo_excel}")
    except Exception as e:
        print(f"Error procesando {archivo_csv}: {e}")