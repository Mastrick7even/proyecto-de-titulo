# models_db/estudiante.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id_estudiante = Column(Integer, primary_key=True)
    rut = Column(String(12), nullable=False, unique=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    año_ingreso = Column(Integer, nullable=False)
    
    id_carrera = Column(Integer, ForeignKey("carreras.id_carrera"), nullable=False)

    # Relaciones: Un estudiante...
    # ... pertenece a una carrera.
    carrera = relationship("Carrera", back_populates="estudiantes")
    # ... tiene muchas inscripciones a asignaturas.
    inscripciones = relationship("Inscripcion", back_populates="estudiante", cascade="all, delete-orphan")
    # ... tiene muchas asistencias a tutorías.
    asistencias = relationship("AsistenciaTutoria", back_populates="estudiante", cascade="all, delete-orphan")
    # ... puede tener muchas alertas.
    alertas = relationship("Alerta", back_populates="estudiante", cascade="all, delete-orphan")
    # ... puede tener un registro de deserción (o ninguno).
    desercion = relationship("Desercion", back_populates="estudiante", uselist=False, cascade="all, delete-orphan")