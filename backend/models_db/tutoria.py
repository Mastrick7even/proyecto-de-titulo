# models_db/tutoria.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base

class Tutoria(Base):
    __tablename__ = "tutorias"

    id_tutoria = Column(Integer, primary_key=True)
    tema = Column(String(255), nullable=True)
    fecha = Column(DateTime, nullable=False)
    
    id_tutor = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)

    # Relaciones
    tutor = relationship("Usuario", back_populates="tutorias_a_cargo")
    asistencias = relationship("AsistenciaTutoria", back_populates="tutoria", cascade="all, delete-orphan")