from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from App.database.database import Base


class Tarea(Base):

    __tablename__ = "tareas"

    id: Mapped[int] = mapped_column(primary_key=True)

    titulo: Mapped[str] = mapped_column()

    descripcion: Mapped[str] = mapped_column()

    completada: Mapped[bool] = mapped_column()

    #foreignkey
    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id")
    )

    #relationship
    usuario: Mapped["Usuario"] = relationship(back_populates="tareas"
    )
