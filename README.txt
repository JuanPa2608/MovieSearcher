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

Secuencia de trabajo:

1- ETL(Extraction Transform Load). Se extrajo la data de gzip en formatdo JSON, se guardo la data ordenada en formatos csv y parquet en la carpeta datasets\New_datasets
Se utilizo: extraccion.ipynb
Librerias: json, gzip, pandas, ast, pdb, numpy y datetime.

2- NLP (Natural Language Processing). Se analizo la columna revies del dataframe user_reviews, se hizo un analisis de sentimientos agregando una columna indicando se era un comentario negativo, neutro o positivo.
Se utilizo: sentimental_analisys.ipynb
Librerias: pandas, nltk.sentiment.vader, SentimentIntensityAnalyzer y pdb

3- Functions for End Points. En base a los nuevos dataframes, se filtro y ordeno los datos para alimentar a la API y responder directamente ocupando menos memoria que los dataframes originales.
Se guardo nuevos dataframes en carpeta 
Se utilizo: datasets_functions.ipynb
Librerias: pandas, ast y pdb

4- EDA (Exploratory data analysis). Se realizo un analisis sobre los nuevos datasets, se presentan caracteristicas de los datos.
Se utilizo: EDA.ipynb
Librerias: pandas, seaborn y matplotlib.pyplot 

Perfil github: https://github.com/JuanPa2608/
Perfil Linkedin: https://www.linkedin.com/in/juan-pablo-espinoza-cortez-977013170/
Link del Web Service: https://steamrecommender.onrender.com/docs