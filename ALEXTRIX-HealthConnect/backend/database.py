from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos desde variables de entorno
# Prioridad 1: DATABASE_URL completa (para Render/producción)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # Prioridad 2: Construir desde variables individuales (desarrollo local)
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASS = os.getenv("DB_PASS", "")
    DB_NAME = os.getenv("DB_NAME", "alextrix_db")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
    # Render usa "postgres://" pero SQLAlchemy 2.0 requiere "postgresql://"
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Configuración de SQLAlchemy con configuración lazy
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Verifica conexión antes de usar
    pool_recycle=300,    # Recicla conexiones cada 5 minutos
    echo=False           # Cambiar a True para debug SQL
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def get_session():
    """Función para obtener una nueva sesión de base de datos"""
    return Session()

def create_tables():
    """Función para crear las tablas - solo cuando se necesite"""
    try:
        Base.metadata.create_all(engine)
        print("✅ Tablas de base de datos creadas/verificadas correctamente")
    except OperationalError as e:
        print(f"⚠️ Error conectando a la base de datos: {e}")
        print("💡 Asegúrate de que PostgreSQL esté ejecutándose o que DATABASE_URL sea correcta")
        return False
    return True

def test_connection():
    """Función para probar la conexión a la base de datos"""
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except OperationalError:
        return False



