# Importación de librerías y extracción de data
import requests
from bs4 import BeautifulSoup
import os
import re
import pandas as pd

# URL de la página
url = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"

# Realizar la solicitud GET a la página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')  # Corregido: sólo una llamada a BeautifulSoup

# Crear una carpeta para almacenar los archivos descargados
os.makedirs('parquet_files', exist_ok=True)

# Función para verificar si el archivo está dentro del rango de años
def is_within_year_range(file_name, start_year, end_year):
    match = re.search(r'(\d{4})', file_name)
    if match:
        year = int(match.group(1))
        return start_year >= year >= end_year
    return False

# Función para extraer mes y año de la ruta del archivo
def obtener_mes_y_ano(file_path):
    match = re.search(r'(\d{4})-(\d{2})', file_path)
    if match:
        año_referencia = int(match.group(1))
        mes_referencia = int(match.group(2))
        return mes_referencia, año_referencia
    else:
        raise ValueError("No se pudo extraer el mes y año del nombre del archivo.")

# Rango de años
start_year = 2022
end_year = 2022

# Inicializar diccionario para almacenar los DataFrames por mes/año
dataframes = {}

# Buscar todos los enlaces de archivos Parquet
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.endswith('.parquet'):
        file_name = href.split('/')[-1]
        # Filtrar solo archivos que contengan 'green_tripdata' o 'yellow_tripdata' y estén en el rango de años
        if ('green_tripdata' in file_name or 'yellow_tripdata' in file_name) and is_within_year_range(file_name, start_year, end_year):
            # Descargar el archivo
            file_url = href
            file_response = requests.get(file_url)
            file_path = os.path.join('parquet_files', file_name)
            with open(file_path, 'wb') as file:
                file.write(file_response.content)
            print(f"Descargado: {file_name}")

            # Leer archivo parquet
            df = pd.read_parquet(file_path)

            # Renombrar las columnas de tiempo para que coincidan
            df = df.rename(columns={
                'lpep_pickup_datetime': 'pickup_time', 
                'lpep_dropoff_datetime': 'dropoff_time',
                'tpep_pickup_datetime': 'pickup_time', 
                'tpep_dropoff_datetime': 'dropoff_time'
            }, inplace=False)

            # Agregar la columna 'type_taxi' basada en el archivo
            df['type_taxi'] = 'green' if 'green_tripdata' in file_name else 'yellow'

            # Extraer solo las columnas requeridas
            df = df[['pickup_time', 'dropoff_time', 'PULocationID', 'DOLocationID', 'trip_distance', 'fare_amount', 'type_taxi']]

            # Extraer la fecha desde pickup_time y agregar una columna 'date'
            df['date'] = pd.to_datetime(df['pickup_time']).apply(lambda x: x.date())
            
            # Convertir las columnas pickup_time y dropoff_time a solo horas
            df['pickup_time'] = pd.to_datetime(df['pickup_time']).dt.time
            df['dropoff_time'] = pd.to_datetime(df['dropoff_time']).dt.time         

            # Extraer el mes y año de referencia del archivo
            mes_referencia, año_referencia = obtener_mes_y_ano(file_path)

            # Filtrar por mes y año
            df_filtrado = df[(pd.to_datetime(df['date']).dt.year == año_referencia) & (pd.to_datetime(df['date']).dt.month == mes_referencia)]

            # Si ya existe un DataFrame para este mes/año, combinarlo con el actual
            if (año_referencia, mes_referencia) in dataframes:
                dataframes[(año_referencia, mes_referencia)] = pd.concat([dataframes[(año_referencia, mes_referencia)], df_filtrado])
            else:
                dataframes[(año_referencia, mes_referencia)] = df_filtrado

# Guardar los DataFrames combinados por cada mes/año
for (año_referencia, mes_referencia), df in dataframes.items():
    # Ordenar el DataFrame por date y pickup_time
    df = df.sort_values(by=['date', 'pickup_time']).reset_index(drop=True)
    
    # Guardar el DataFrame final filtrado y ordenado en un archivo parquet
    output_file_name = f"trip_data_filtrado_{año_referencia}-{mes_referencia:02d}.parquet"
    df.to_parquet(output_file_name, index=False)
    print(f"Guardado: {output_file_name}")

print("Descarga y procesamiento completado.")


