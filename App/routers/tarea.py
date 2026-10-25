from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App.database.database import get_db

from App.models.tarea import Tarea
from App.models.usuario import Usuario

from App.schemas.tarea import TareaResponse, TareaCreate


router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)

@router.get("/", response_model=list[TareaResponse])
def listar_tareas(
    db: Session = Depends(get_db)
):
    tareas = db.query(Tarea).all()
    return tareas


@router.post(
    "/", response_model=TareaResponse, status_code=201
)
def crear_tarea(
    datos: TareaCreate,
    db: Session = Depends(get_db)
):

    usuario = db.query(Usuario).filter(
        Usuario.id == datos.usuario_id
    ).first()

    if usuario is None:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

    nueva_tarea = Tarea(
        titulo=datos.titulo,
        descripcion=datos.descripcion,
        completada=datos.completada,
        usuario_id=datos.usuario_id
    )

    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)

    return nueva_tarea


@router.get(
     "/{tarea_id}",
     response_model=TareaResponse
)
def buscar_tarea(
    tarea_id: int,
    db: Session = Depends(get_db)
):
    tarea = db.query(Tarea).filter(
        Tarea.id == tarea_id
    ).first()

    if tarea is None:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    return tarea

@router.put(
     "/{tarea_id}",
     response_model=TareaResponse
)
def actualizar_tarea(
    tarea_id: int,
    datos: TareaCreate,
    db: Session = Depends(get_db)
):
    tarea = db.query(Tarea).filter(
        Tarea.id == tarea_id
    ).first()

    if tarea is None:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    usuario = db.query(Usuario).filter(
        Usuario.id == datos.usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    tarea.titulo = datos.titulo
    tarea.descripcion = datos.descripcion
    tarea.completada = datos.completada
    tarea.usuario_id = datos.usuario_id

    db.commit()
    db.refresh(tarea)

    return tarea

@router.delete(
     "/{tarea_id}"
)
def eliminar_tarea(
     tarea_id: int,
     db: Session = Depends(get_db)
):
    tarea = db.query(Tarea).filter(
        Tarea.id == tarea_id
    ).first()

    if tarea is None:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    db.delete(tarea)
    db.commit()

    return {
           "mensaje": "Tarea eliminada correctamente"
        }
