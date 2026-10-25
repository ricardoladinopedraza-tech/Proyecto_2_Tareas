from pydantic import BaseModel, ConfigDict

class TareaCreate(BaseModel):
    titulo: str
    descripcion: str
    completada: bool
    usuario_id: int

class TareaResponse(BaseModel):
    id: int
    titulo: str
    descripcion: str
    completada: bool
    usuario_id: int

    model_config = ConfigDict(from_attributes=True)