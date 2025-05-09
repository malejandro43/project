import pandas as pd
import numpy as np
atlas = [
      ['France', 'Paris'],  
        ['Russia', 'Moscow'],  
        ['China', 'Beijing'],  
        ['Mexico', 'Mexico City'],  
        ['Egypt', 'Cairo'],
]
geography = ['country', 'capital']#le asigna a una lista nombres de columnas


# creamos un DataFrame
world_map = pd.DataFrame(data=atlas , columns=geography)

# mostrando el DataFrame
#print(world_map)
print(world_map.info())


df = pd.read_csv('/datasets/music_log_chpt_11.csv')

data_types =df.dtypes  # escribe tu código aquí Utiliza el atributo dtypes para conocer los tipos de datos de las columnas del DataFrame df. Almacena el resultado en la variable data_types y muéstralo.

print(data_types)


df = pd.read_csv('/datasets/music_log_chpt_11.csv')

column_names =df.columns # escribe tu código aquí Utiliza el atributo columns para obtener los nombres de todas las columnas en el DataFrame df. Almacena el resultado en la variable column_names y muéstralo.



print(column_names)



df = pd.read_csv('/datasets/music_log_chpt_11.csv')

data_shape = df.shape # escribe tu código aquí Utiliza el atributo shape para obtener las dimensiones (filas y columnas) del DataFrame df. Almacena el resultado en la variable data_shape y muéstralo.



print(data_shape)



df = pd.read_csv('/datasets/music_log_chpt_11.csv')#xUtiliza el método info() para mostrar un resumen del DataFrame df. No es necesario almacenar el resultado, simplemente utiliza el método para obtener la información.


print(df.info())



data = {'product_id': [101, 102, 103],
        'product_name': ['Laptop', 'Smartphone', 'Tablet'],
        'price': [1500, 800, 300],
        'category': ['Electronics', 'Electronics', 'Electronics']}

df = pd.DataFrame(data)

data_shape = df.shape# escribe tu código aquí Como parte de tu análisis, necesitas verificar si la cantidad de productos en la tienda es la correcta. Utiliza shape para verificar el tamaño del DataFrame y info() para asegurarte de que todas las columnas tienen 3 filas completas.
print(data_shape)
df.info()

# Escribe tu código aquí para mostrar la información del DataFrame
