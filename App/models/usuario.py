from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from App.database.database import Base

#modelo ORM
class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)  #Estilo clasico de SQLAlchemy

    nombre: Mapped[str] = mapped_column(nullable=False)

    correo: Mapped[str] = mapped_column(nullable=False, unique=True)

    #relationship
    tareas: Mapped[list["Tarea"]] = relationship(back_populates="usuario"
    )
