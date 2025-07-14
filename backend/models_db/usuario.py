# models_db/usuario.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True)
    rut = Column(String(12), nullable=False, unique=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False) # 'tutor' o 'encargado_carrera'

    # Relaciones: Un usuario puede...
    # ... ser el tutor a cargo de muchas tutorías.
    tutorias_a_cargo = relationship("Tutoria", back_populates="tutor")
    # ... crear muchas alertas.
    alertas_creadas = relationship("Alerta", back_populates="creador")