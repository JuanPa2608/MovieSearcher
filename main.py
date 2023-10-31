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
    lista = df_UserForGenre[genre]['user']
    return str('Usuario con más horas jugadas para Género: ' + genre + ' Horas jugadas: ' + str(anio))


