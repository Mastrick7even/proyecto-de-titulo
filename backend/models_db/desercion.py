# models_db/desercion.py

from sqlalchemy import Column, Integer, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class Desercion(Base):
    __tablename__ = "deserciones"

    # La PK es también la FK, lo que garantiza una relación 1 a 1 con estudiantes.
    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"), primary_key=True)
    fecha_desercion = Column(Date, nullable=False)
    razon = Column(Text, nullable=True)

    # Relación
    estudiante = relationship("Estudiante", back_populates="desercion")