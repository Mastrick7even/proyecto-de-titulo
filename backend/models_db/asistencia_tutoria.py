# models_db/asistencia_tutoria.py

from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class AsistenciaTutoria(Base):
    __tablename__ = "asistencias_tutorias"

    id_asistencia = Column(Integer, primary_key=True)
    id_tutoria = Column(Integer, ForeignKey("tutorias.id_tutoria"), nullable=False)
    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False)

    # Relaciones
    tutoria = relationship("Tutoria", back_populates="asistencias")
    estudiante = relationship("Estudiante", back_populates="asistencias")

    # Restricción para que un estudiante no asista dos veces a la misma tutoría
    __table_args__ = (UniqueConstraint('id_tutoria', 'id_estudiante', name='_tutoria_estudiante_uc'),)