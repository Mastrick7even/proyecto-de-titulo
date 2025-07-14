# models_db/alerta.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class Alerta(Base):
    __tablename__ = "alertas"

    id_alerta = Column(Integer, primary_key=True)
    tipo_alerta = Column(String(50), nullable=False) # 'Formal Programa' o 'Espontánea Tutor'
    descripcion = Column(Text, nullable=False)
    estado = Column(String(50), nullable=False, default='abierta') # 'abierta', 'en_proceso', 'cerrada'
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    
    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False)
    id_usuario_creador = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="alertas")
    creador = relationship("Usuario", back_populates="alertas_creadas")