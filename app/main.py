from fastapi import FastAPI
from app.core.config import settings
from app.routers import health # Importamos nuestro nuevo router

# Crea una instancia de la aplicación FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

# Incluye el router en la aplicación principal.
# Ahora todos los endpoints de health.py estarán disponibles.
app.include_router(health.router)


@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint principal.
    """
    return {"mensaje": "¡Bienvenido al Sistema de Alerta Temprana (SAT)!"}