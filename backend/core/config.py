import os
from dotenv import load_dotenv

# Carga las variables de entorno del archivo .env
# Esto es útil para el desarrollo local.
load_dotenv()

class Settings:
    """
    Clase para gestionar la configuración de la aplicación.
    Lee las variables de entorno.
    """
    PROJECT_NAME: str = "Sistema de Alerta Temprana (SAT)"
    PROJECT_VERSION: str = "0.1.0"

    # Configuración de la Base de Datos
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")

    # La URL completa de la base de datos se construye a partir de las variables
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Creamos una instancia de la configuración para ser usada en toda la app
settings = Settings()