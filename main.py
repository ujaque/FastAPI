from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def _root():
    return "Hola fastAPi"


@app.get("/url")
async def _root():
    return {"url_curso":"ujaque.es"}