from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/inicio")
async def ruta_prueba():
    return "Hola"

df_PlayTimeGenre = pd.read_parquet('datasets/PlayTimeGenre.parquet')

@app.get("/PlayTimeGenre")
async def PlayTimeGenre(genre):
    anio = df_PlayTimeGenre['release_year'][df_PlayTimeGenre['Sum_playtime_forever'][df_PlayTimeGenre['genres'] == genre].idxmax()]
    return str('Año de lanzamiento con más horas jugadas para Género ' + genre + ': ' + str(anio))

df_UserForGenre = pd.read_csv('datasets/UserForGenre.csv')

@app.get("/UserForGenre")
async def UserForGenre(genre):
    user = df_UserForGenre[genre][0]
    lista = df_UserForGenre[genre][1]
    return str('Usuario con más horas jugadas para Género ' + genre + ': ' + user + ' Horas jugadas: ' + lista)

df_UsersRecommend = pd.read_parquet('datasets/UsersRecommend.parquet')

@app.get("/UsersRecommend")
async def UsersRecommend(anio):
    top_recomend = df_UsersRecommend[df_UsersRecommend['year_posted'] == anio]
    top_recomend.reset_index(drop = True,inplace = True)
    #return str('Items_id Puesto 1: '+ top_recomend['item_id'][0] + ' Puesto 2: '+ top_recomend['item_id'][1] + ' Puesto 3: '+ top_recomend['item_id'][2])
    return df_UsersRecommend
    

