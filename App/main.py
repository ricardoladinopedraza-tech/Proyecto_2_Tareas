#importar FastAPI
from fastapi import FastAPI

from App.routers.usuario import router as usuario_router #importar router usuario
from App.routers.tarea import router as tarea_router #importar router tarea

from App.models.usuario import Usuario
from App.models.tarea import Tarea


#Crear instancia de la aplicacion
app = FastAPI()

#registramos el router usuario con nombre usuario_router
app.include_router(usuario_router)
#registramos el router tarea con el nombre tarea_router
app.include_router(tarea_router)


#Crear primer endpoint GET /
@app.get("/")
def inicio():
    return { "mensaje": "API Proyecto 2 funcionando"}
