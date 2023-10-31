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
    return int(anio)
