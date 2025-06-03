# Usa una imagen oficial de Python como base
FROM python:3.10-slim-bullseye

# Actualiza los paquetes del sistema para reducir vulnerabilidades
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Establece variables de entorno para Python para optimizar
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Opcional: Instala dependencias del sistema si fueran necesarias
# Por ejemplo, a veces para psycopg2 (PostgreSQL) se necesita gcc y libpq-dev
# Si encuentras errores de compilación de psycopg2, descomenta la siguiente línea:
# RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copia el archivo de requerimientos ANTES de copiar el resto del código
# Esto aprovecha el caché de Docker si los requerimientos no cambian
COPY requirements.txt .

# Instala las dependencias Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el directorio de tu aplicación (donde está tu código FastAPI)
# Asumimos que tu código está en una carpeta llamada 'app' en la raíz de tu proyecto
COPY ./app /app/app
# Si tienes una carpeta 'ml' con modelos o scripts que la API necesita y quieres incluirla en la imagen:
# COPY ./ml /app/ml

# Expone el puerto en el que correrá tu aplicación FastAPI (Uvicorn por defecto usa 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor inicie
# Asegúrate que 'app.main:app' coincida con la ubicación de tu archivo principal
# y la instancia de FastAPI. Ej: si tu archivo es 'app/api_entrypoint.py' y tu app es 'my_api = FastAPI()',
# sería 'app.api_entrypoint:my_api'.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]