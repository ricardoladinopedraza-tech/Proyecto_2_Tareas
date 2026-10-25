from pydantic import BaseModel, ConfigDict

class UsuarioCreate(BaseModel):
    nombre: str
    correo: str

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: str

    model_config = ConfigDict(from_attributes=True)
