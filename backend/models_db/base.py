# models_db/base.py

from sqlalchemy.orm import declarative_base

# Se crea una clase Base que nuestros modelos ORM heredarán.
# SQLAlchemy usará esta base para relacionar las clases con las tablas.
Base = declarative_base()