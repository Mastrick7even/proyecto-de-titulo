from fastapi import APIRouter

# Creamos un "router". Es como una mini-aplicación de FastAPI.
# Lo usaremos para agrupar todos los endpoints relacionados.
router = APIRouter(
    prefix="/health", # Todos los endpoints en este router empezarán con /health
    tags=["Health Check"] # Así se agrupará en la documentación de Swagger
)

@router.get("/")
def health_check():
    """
    Endpoint simple para verificar que la API está viva.
    """
    return {"status": "ok", "message": "API is running!"}