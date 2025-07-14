# models_db/inscripcion.py

from sqlalchemy import Column, Integer, Numeric, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Inscripcion(Base):
    __tablename__ = "inscripciones"

    id_inscripcion = Column(Integer, primary_key=True)
    calificacion_final = Column(Numeric(3, 1), nullable=True) # Permite notas como 4.5
    
    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False)
    id_asignatura = Column(Integer, ForeignKey("asignaturas.id_asignatura"), nullable=False)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="inscripciones")
    asignatura = relationship("Asignatura")
    
    # Restricción para que un estudiante no se inscriba dos veces en la misma asignatura
    __table_args__ = (UniqueConstraint('id_estudiante', 'id_asignatura', name='_estudiante_asignatura_uc'),)