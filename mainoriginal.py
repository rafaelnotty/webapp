from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import importlib.util

app = FastAPI()

# Habilitar la carpeta "static" para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Cargar el módulo validador.py
spec = importlib.util.spec_from_file_location("validador", "validador.py")
validador = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validador)

@app.get("/", response_class=FileResponse)
async def read_item():
    return "static/index.html"

class Mensaje(BaseModel):
    mensaje: str

@app.post("/enviar-mensaje/")
async def enviar_mensaje(mensaje: Mensaje):
    respuesta = validador.contador.validar_mensaje(mensaje.mensaje)
    return {"respuesta": respuesta}
