# models_db/__init__.py

from .base import Base
from .usuario import Usuario
from .carrera import Carrera
from .estudiante import Estudiante
from .asignatura import Asignatura
from .inscripcion import Inscripcion
from .tutoria import Tutoria
from .asistencia_tutoria import AsistenciaTutoria
from .alerta import Alerta
from .desercion import Desercion

# Opcional: puedes definir una lista __all__ para controlar lo que se importa con 'from models_db import *'
__all__ = [
    "Base",
    "Usuario",
    "Carrera",
    "Estudiante",
    "Asignatura",
    "Inscripcion",
    "Tutoria",
    "AsistenciaTutoria",
    "Alerta",
    "Desercion",
]