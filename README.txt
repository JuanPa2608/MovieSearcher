Proyecto STEAM

El proyecto es un sistema de recomendacion de videojuegos basada en una data por usuarios, generos jugados
y los tiempos jugados a lo largo de los años.

Los juegos tienen una clara preferencia por el genero Accion, siendo este el mas jugado. 

Los usuarios en general son un publico un tanto dificil, pero aun indeciso sobre la calidad del videojuego.

Se ha utilizado las librerias:

json: Una vez descomprimida la data se presentan datos en formato json.
gzip: Utilizado para descomprimir directamente la Base de Datos principal (Steam)
numpy: Libreria matematica basica utilizada para completar datos vacios por nan.
datetime: Libreria para trabajar con fechas. Las fechas se presentaban completas y se requeria unicamente el año.
pandas: Libreria para trabajar con lectura, manipulacion y guardado de dataframes.
ast:Convierte cada línea JSON (texto) en un diccionario de Python, los datos se presentan en este formato.
pdb: Debugger que simplifica el encontrar errores en el codigo.
nltk.sentiment.vader: Procesador de Lenguaje Natural (NPL) analisis de sentimiento. Evalua los reviews de los usuarios y detecta una tendencia.
seaborn: Libreria utilizada para graficos EDA
matplotlib.pyplot: Libreria utilizada para graficos EDA

github: https://github.com/JuanPa2608