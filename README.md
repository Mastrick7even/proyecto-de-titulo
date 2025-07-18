# Sistema de Alerta Temprana para la Prevención de la Deserción de Estudiantes de Primer Año Universitario Utilizando Modelos Predictivos

## 📝 Descripción

Este proyecto de título tiene como objetivo principal desarrollar e implementar un sistema inteligente para **apoyar la detección temprana de estudiantes de primer año en riesgo de deserción** en la Facultad de Ciencias Empresariales (FACE) de la Universidad del Bío-Bío. Mediante el uso de técnicas de aprendizaje automático, el sistema analizará datos históricos y actuales para generar indicadores de riesgo, que se presentarán a través de un dashboard interactivo y reportes automatizados. La finalidad es proveer una herramienta de apoyo a los encargados de carrera y tutores del Programa de Tutores institucional, facilitando intervenciones más oportunas y personalizadas para mejorar la retención estudiantil.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje de Programación:** Python 3.10+
* **Framework Backend (API):** FastAPI
* **Servidor ASGI:** Uvicorn
* **Base de Datos:** PostgreSQL
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Contenerización:** Docker, Docker Compose
* **Frontend/Dashboard:** _(Por definir, se evaluará Plotly Dash o Streamlit)_
* **Control de Versiones:** Git, GitHub

## 🏛️ Arquitectura del Proyecto (General)

El sistema se compone de los siguientes elementos principales:
1.  **API Backend (FastAPI):** Encargada de la lógica de negocio, procesamiento de datos, interacción con la base de datos y ejecución de los modelos de Machine Learning.
2.  **Base de Datos (PostgreSQL):** Almacena los datos históricos de los estudiantes, datos del programa de tutores, y los resultados/predicciones del modelo.
3.  **Módulo de Machine Learning:** Componente (integrado en la API) que contiene los modelos entrenados para predecir el riesgo de deserción.
4.  **Frontend/Dashboard:** Interfaz web para que los tutores y encargados de carrera visualicen los niveles de riesgo, alertas y reportes.

## 🌳 Modelo de Ramificación (Git Branching Model)

Este proyecto utilizará un modelo de ramificación simple pero efectivo:

* **`main`**: Esta rama siempre contendrá la versión más estable y probada del proyecto. Corresponderá a las versiones "entregables" o listas para una demostración. No se hacen pushes directos a `main`. Las fusiones a `main` se realizan exclusivamente desde la rama `develop` mediante Pull Requests aprobados.
* **`develop`**: Es la rama principal de integración para nuevas funcionalidades. Todo el desarrollo activo y las nuevas características se fusionan primero aquí (desde ramas `feature/*`). Esta rama debe mantenerse funcional, ya que representa el estado más actualizado del proyecto en desarrollo.
* **`feature/<nombre-descriptivo>`**: Para cada nueva funcionalidad, mejora o corrección de error significativa, se creará una nueva rama a partir de `develop`.
    * Ejemplos: `feature/setup-database-models`, `feature/ml-prediction-endpoint`, `fix/login-bug`.
    * Una vez completado el trabajo en una rama `feature/*` y probada (idealmente), se crea un Pull Request para fusionarla a `develop`.

## 🚀 Configuración y Uso (Desarrollo Local)

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_AQUI>
    cd <NOMBRE_DEL_PROYECTO>
    ```
2.  **Configurar Variables de Entorno:**
    * Copiar el archivo `.env.example` a un nuevo archivo llamado `.env`:
        ```bash
        cp .env.example .env
        ```
    * Editar el archivo `.env` con las credenciales y configuraciones necesarias (especialmente para PostgreSQL).
3.  **Construir e Iniciar los Contenedores Docker:**
    * Asegúrate de tener Docker y Docker Compose instalados y el servicio Docker corriendo.
    * Desde la raíz del proyecto, ejecuta:
        ```bash
        docker compose up --build -d
        ```
        (La opción `-d` lo ejecuta en segundo plano o "detached mode")
4.  **Acceder a la API:**
    * La API estará disponible en `http://localhost:8000`.
    * Puedes ver la documentación interactiva de la API (Swagger UI) en `http://localhost:8000/docs`.
    * Y la documentación alternativa (ReDoc) en `http://localhost:8000/redoc`.
5.  **Para detener los servicios:**
    ```bash
    docker compose down
    ```