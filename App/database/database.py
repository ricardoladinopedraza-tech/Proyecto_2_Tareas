#Imports necesarios
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#Buscamos .env y cargamos su informacion
load_dotenv()

#Obtenemos DATABASE_URL desde el entorno
DATABASE_URL = os.getenv("DATABASE_URL")

#Creamos engine
engine = create_engine(DATABASE_URL)

#crear sesion local
SessionLocal = sessionmaker(bind=engine)

#Creamos BAse
class Base(DeclarativeBase):
    pass

#GEnerador de conexiones, abre y cierra la comunicacion con la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()