# models_db/carrera.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Carrera(Base):
    __tablename__ = "carreras"

    id_carrera = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False, unique=True)
    
    # Opcional: Si quieres un vínculo directo al encargado.
    id_encargado = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=True)

    # Relaciones: Una carrera...
    # ... tiene muchos estudiantes.
    estudiantes = relationship("Estudiante", back_populates="carrera")