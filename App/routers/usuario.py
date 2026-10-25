from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from App.database.database import get_db
from App.models.usuario import Usuario
from App.models.tarea import Tarea

from App.schemas.usuario import UsuarioCreate, UsuarioResponse

from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/")
def listar_usuarios(
    db: Session = Depends(get_db)
):
    usuarios = db.query(Usuario).all()
    return usuarios

#endpoint crear usuario
@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(
    datos: UsuarioCreate,
    db: Session = Depends(get_db)
):
    nuevo_usuario = Usuario(
        nombre=datos.nombre,
        correo=datos.correo
    )

    try:
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)


    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Correo ya registrado"
        )

    return nuevo_usuario

#Endpoint para buscar un usuario con id
@router.get(
    "/{usuario_id}",
    response_model=UsuarioResponse
)
def buscar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario

#Endpoint actualizar usuario
@router.put(
    "/{usuario_id}",
    response_model=UsuarioResponse
)
def actualizar_usuario(
    usuario_id: int,
    datos: UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    try:
        usuario.nombre = datos.nombre    #estos dos se pueden dejar por fuera del try
        usuario.correo = datos.correo
        db.commit()
        db.refresh(usuario)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Correo ya registrado"
        )

    return usuario

#endpoint Delete
@router.delete(
    "/{usuario_id}"
)
def eliminar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
            Usuario.id == usuario_id
        ).first()

    if usuario is None:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

    tarea_asociada = db.query(Tarea).filter(
        Tarea.usuario_id == usuario_id
    ).first()

    if tarea_asociada is not None:
        raise HTTPException(
            status_code=409,
            detail="No se puede eliminar el usuario porque tiene tareas asociadas"
        )

    db.delete(usuario)
    db.commit()

    return {"mensaje": "Usuario eliminado correctamente"}
