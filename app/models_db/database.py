from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings # Importamos nuestra configuración

# Creamos el motor de la base de datos usando la URL de la configuración
engine = create_engine(settings.DATABASE_URL)

# Creamos una fábrica de sesiones (SessionLocal) que usaremos para crear sesiones de BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base es una clase base para nuestros modelos de SQLAlchemy (las tablas de la BD)
Base = declarative_base()

# --- Dependencia para las rutas ---
def get_db():
    """
    Función de dependencia de FastAPI que crea y gestiona una sesión de base de datos.
    Se asegura de que la sesión se cierre siempre, incluso si hay un error.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()