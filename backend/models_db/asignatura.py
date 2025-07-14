# models_db/asignatura.py

from sqlalchemy import Column, Integer, String
from .base import Base

class Asignatura(Base):
    __tablename__ = "asignaturas"

    id_asignatura = Column(Integer, primary_key=True)
    codigo = Column(String(20), nullable=False, unique=True)
    nombre = Column(String(255), nullable=False)
    semestre = Column(Integer, nullable=False) # 1 o 2