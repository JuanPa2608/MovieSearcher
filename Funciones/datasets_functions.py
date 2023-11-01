
# <center><b>Funciones para Endspoints (API)<b><center>

# Importacion de librerias
import pandas as pd
import ast

# Carga de datasets
df_items = pd.read_parquet('..\\datasets\\New_datasets\\user_items.parquet')
df_reviews = pd.read_parquet('..\\datasets\\New_datasets\\user_reviews_sentiments.parquet')
df_steams = pd.read_csv('..\\datasets\\New_datasets\\user_steams.csv')

df_items['steam_id'] = df_items['steam_id'].apply(float)
df_items.info()

# %% [markdown]
# <b>PlayTimeGenre:</b>       
# 
# Debe devolver año con mas horas jugadas para dicho género.

# Se eliminan los datos nulos de las columnas a consultar
df_steams_genre = df_steams.dropna(subset='genres')
df_steams_genre.reset_index(inplace=True,drop=True)
df_steams_genre = df_steams_genre.dropna(subset='release_year')
df_steams_genre.reset_index(inplace=True,drop=True)
df_steams_genre.info()

# Desanidado de columna genres de dataset df_steams_genre
datos = []
def genre_reader(df_genre):
    try:
        for index,line in enumerate(df_genre['genres']):
            dato_genres = ast.literal_eval(line) 
            #pdb.set_trace()
            for genre in dato_genres:
                #pdb.set_trace()
                datos.append([genre,df_genre['release_year'][index],df_genre['app_name'][index],df_genre['title'][index]])
    except:
        pdb.set_trace()

    return pd.DataFrame(datos,columns=['genres','release_year','app_name','title'])

# Se observa que se presentan columna duplicadas
df_PlayTimeGenre = genre_reader(df_steams_genre)
# Se trabaja con una de las columnas nombre y se rescata solo las columnas de interes
df_PlayTimeGenre = df_PlayTimeGenre.merge(df_items,left_on='title', right_on='item_name')
df_PlayTimeGenre = df_PlayTimeGenre[['genres','release_year','playtime_forever']]

# Se agrupa 'genres','release_year' y se suma la columna 'playtime_forever' segun lo solicitado. 
# Se utiliza la funcion transform para especificar el contenido de la nueva columna
df_PlayTimeGenre['Sum_playtime_forever'] = df_PlayTimeGenre.groupby(['genres','release_year'])['playtime_forever'].transform('sum')

# Se elimina la columna 'playtime_forever' que ya se utilizo para la suma y se quita duplicados generados en group by
df_PlayTimeGenre.drop(columns='playtime_forever',inplace=True)
df_PlayTimeGenre.drop_duplicates(subset=['genres','release_year'],inplace=True)
df_PlayTimeGenre.reset_index(drop=True,inplace=True)
df_PlayTimeGenre.info()
df_PlayTimeGenre.head(3)

# Funcion de consulta por genero el año de mayor cantidad de horas acumuladas
def PlayTimeGenre(genre):
    anio = df_PlayTimeGenre['release_year'][df_PlayTimeGenre['Sum_playtime_forever'][df_PlayTimeGenre['genres'] == genre].idxmax()]
    return int(anio)

df_PlayTimeGenre[df_PlayTimeGenre['genres'] == 'Action'][df_PlayTimeGenre['genres'] == 'Action']

# Prueba
PlayTimeGenre('Action')

# %% [markdown]
# <b>UserForGenre:</b>       
# 
# Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año. Es similar la funcion PlayTimeGenre, pero se agrega usuario y lista de juegos con horas jugadas

# Consulta de generos desanidados y merge con dataframe items
df_UserForGenre = genre_reader(df_steams_genre)
df_UserForGenre = df_UserForGenre.merge(df_items,left_on='title', right_on='item_name')
df_UserForGenre = df_UserForGenre[['genres','user_id','release_year','playtime_forever']]


# Agrupado segun lo requerido
df_UserForGenre_group = df_UserForGenre.copy()
df_UserForGenre_group['Sum_playtime_year'] = df_UserForGenre_group.groupby(['genres','user_id','release_year'])['playtime_forever'].transform('sum')
df_UserForGenre_group.drop(columns='playtime_forever',inplace=True)
df_UserForGenre_group.drop_duplicates(subset=['genres','user_id','release_year'],inplace=True)
df_UserForGenre_group.reset_index(drop=True,inplace=True)

df_UserForGenre_group.head(3)

df_genres = df_UserForGenre_group['genres']
df_genres.drop_duplicates(inplace=True)
df_genres.reset_index(drop=True,inplace=True)
df_genres

# Funcion de agrupamiento y consulta
def UserForGenre(genre):
    # Captando el maximo de tiempo
    user = df_UserForGenre_group['user_id'][df_UserForGenre_group['Sum_playtime_year'][df_UserForGenre_group['genres'] == genre].idxmax()]
    lista = df_UserForGenre_group[df_UserForGenre_group['genres'] == genre][df_UserForGenre_group['user_id'] == user]
    lista = lista[['release_year','Sum_playtime_year']]
    lista.sort_values(by = ['release_year'], inplace = True)
    lista.reset_index(drop = True,inplace = True)
    return {'user' : user, 'lista' : lista}

UserForGenre('Indie')


def UserForGenre_total():
    return {genre: UserForGenre(genre) for genre in df_genres}
df_UserForGenre_Total = UserForGenre_total()

df_UserForGenre_Total.get('Indie')

df_UserForGenre = pd.DataFrame(df_UserForGenre_Total)
df_UserForGenre

# %% [markdown]
# <b>UsersRecommend:</b>       
# 
# Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

df_reviews_recomend = df_reviews.dropna(subset='recommend')
df_reviews_recomend.reset_index(drop=True,inplace=True)
df_reviews_recomend.info()
df_reviews_recomend.head()

df_UsersRecommend = df_reviews_recomend[['item_id','recommend','year_posted']].copy()
df_UsersRecommend = df_UsersRecommend[df_UsersRecommend['recommend']]

df_UsersRecommend['Recomends_times'] = df_UsersRecommend.groupby(['item_id','year_posted'])['item_id'].transform('count')
df_UsersRecommend.drop_duplicates(subset=['item_id','year_posted','Recomends_times'],inplace=True)
df_UsersRecommend.reset_index(drop=True,inplace=True)

df_UsersRecommend.sort_values(by='Recomends_times',ascending=False,inplace=True)
df_UsersRecommend.head()

# Funcion de consulta
def UsersRecommend(anio):
    top_recomend = df_UsersRecommend[df_UsersRecommend['year_posted'] == anio]
    return top_recomend['item_id'].head(3)

UsersRecommend(2014)

# Funcion de consulta
def UsersNotRecommend(anio):
    top_not_recomend = df_UsersRecommend[df_UsersRecommend['year_posted'] == anio]
    return top_not_recomend['item_id'].tail(3)

UsersNotRecommend(2014)

# %% [markdown]
# <b>sentiment_analysis:</b>       
# 
# Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

df_reviews.head()

df_SentimentRecommend = df_reviews[['item_id','year_posted','sentiment_analysis']].copy()

# Agrupando por 'year_posted','sentiment_analysis' y contando la cantidad de datos
df_SentimentRecommend['Recomends_times'] = df_SentimentRecommend.groupby(['item_id','year_posted','sentiment_analysis'])['year_posted'].transform('count')
df_SentimentRecommend.drop_duplicates(subset=['item_id','year_posted','sentiment_analysis'],inplace=True)
df_SentimentRecommend.sort_values(by='sentiment_analysis',ascending=True,inplace=True)
df_SentimentRecommend.reset_index(drop=True,inplace=True)


# Cambiando contenido de sentiment_analysis
df_SentimentRecommend['sentiment_analysis'].replace(0,'Negative',inplace=True)
df_SentimentRecommend['sentiment_analysis'].replace(1,'Neutral',inplace=True)
df_SentimentRecommend['sentiment_analysis'].replace(2,'Positive',inplace=True)

df_SentimentRecommend

df_SentimentRecommend.info()

anio = 2014
analisis_sentimiento = df_SentimentRecommend[df_SentimentRecommend['year_posted'] == anio]
analisis_sentimiento.count()

def sentiment_analysis(anio):
    analisis_sentimiento = df_SentimentRecommend[df_SentimentRecommend['year_posted'] == anio]

    return print('Negative: ', analisis_sentimiento['sentiment_analysis'][analisis_sentimiento['sentiment_analysis'] == 'Negative'].count(),
                 'Neutral: ', analisis_sentimiento['sentiment_analysis'][analisis_sentimiento['sentiment_analysis'] == 'Neutral'].count(),
                 'Positive: ', analisis_sentimiento['sentiment_analysis'][analisis_sentimiento['sentiment_analysis'] == 'Positive'].count())

sentiment_analysis(2014)

# %% [markdown]
# <b>Guardar dataframes para Funciones</b>

df_PlayTimeGenre.to_parquet('..\\Funciones\\datasets\\PlayTimeGenre.parquet',index=False)
df_UserForGenre.to_csv('..\\Funciones\\datasets\\UserForGenre.csv',index=False)
#df_UserForGenre.to_parquet('..\\Funciones\\datasets\\UserForGenre.parquet',index=False)
df_UsersRecommend.to_parquet('..\\Funciones\\datasets\\UsersRecommend.parquet',index=False)
df_SentimentRecommend.to_parquet('..\\Funciones\\datasets\\SentimentRecommend.parquet',index=False)


