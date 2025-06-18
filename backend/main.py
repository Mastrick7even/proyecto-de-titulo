from fastapi import FastAPI
from fastapi.responses import FileResponse # <<--- AÑADE ESTA IMPORTACIÓN
import pathlib # <<--- AÑADE ESTA IMPORTACIÓN
from backend.core.config import settingsgit
from backend.routers import health # Importamos nuestro nuevo router


# Define la ruta base del proyecto para construir rutas a archivos estáticos
# Asumimos que este main.py está en backend/main.py o backend/core/main.py
# Y que 'static' está en backend/static/
# Si main.py está en backend/core/main.py, entonces static_dir será backend/static
# Si main.py está en backend/main.py, entonces static_dir será backend/static
BASE_DIR = pathlib.Path(__file__).resolve().parent 
STATIC_DIR = BASE_DIR / "static"

# Crea una instancia de la aplicación FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

# Incluye el router en la aplicación principal.
# Ahora todos los endpoints de health.py estarán disponibles.
app.include_router(health.router)

# Endpoint para servir el favicon.ico
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    favicon_path = STATIC_DIR / "favicon.ico"
    if favicon_path.exists():
        return FileResponse(favicon_path)
    else:
        return {"detail": "Favicon not found"}, 404

@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint principal.
    """
    return {"mensaje": "¡Bienvenido al Sistema de Alerta Temprana (SAT)!"}