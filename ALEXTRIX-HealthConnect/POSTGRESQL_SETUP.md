# 🐘 Configuración de PostgreSQL Local

## Para Desarrollo Local (Opcional)

Si quieres probar localmente con PostgreSQL antes de subir a Render:

### 📥 Instalación PostgreSQL

**Windows:**
1. Descarga: https://www.postgresql.org/download/windows/
2. Instala PostgreSQL (versión 16 recomendada)
3. Durante instalación:
   - Puerto: `5432` (default)
   - Password: (elige una contraseña, la necesitarás)
   - Locale: Spanish_Spain

**Mac:**
```bash
brew install postgresql@16
brew services start postgresql@16
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

---

### 🔧 Configurar Base de Datos

**Opción 1: Usar pgAdmin (GUI - Más fácil)**

1. Abre pgAdmin (se instaló con PostgreSQL)
2. Conecta al servidor local (password que configuraste)
3. Right-click "Databases" → Create → Database
4. Nombre: `alextrix_db`
5. Listo

**Opción 2: Usar terminal/psql (Avanzado)**

```bash
# Windows: Abrir "SQL Shell (psql)"
# Mac/Linux: abrir terminal

# Crear base de datos
createdb alextrix_db

# O conectarse a PostgreSQL
psql -U postgres
CREATE DATABASE alextrix_db;
\q
```

---

### 📝 Configurar archivo .env

Crea el archivo `.env` en `ALEXTRIX-HealthConnect/`:

```env
# PostgreSQL Local
DB_USER=postgres
DB_PASS=tu_password_de_postgres
DB_NAME=alextrix_db
DB_HOST=localhost
DB_PORT=5432
```

⚠️ Reemplaza `tu_password_de_postgres` con la contraseña que configuraste durante la instalación.

---

### ✅ Verificar instalación

```powershell
# Instalar dependencias Python
pip install -r requirements.txt

# Ejecutar servidor
cd ALEXTRIX-HealthConnect
uvicorn main:app --reload
```

Si todo está bien, verás:
```
✅ Tablas de base de datos creadas/verificadas correctamente
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## 🚀 Alternativa: Saltar PostgreSQL Local

**Recomendación:** Si solo quieres subir a Render, NO necesitas instalar PostgreSQL localmente.

Simplemente:
1. Sube el código a GitHub
2. Crea PostgreSQL en Render (gratis)
3. Despliega el Web Service
4. Render se encarga del resto

---

## 🔌 Para Render (Producción)

**NO necesitas crear archivo .env en Render.**

Render provee automáticamente `DATABASE_URL` cuando creas una base de datos PostgreSQL.

Solo necesitas:
1. Crear PostgreSQL en Render
2. Copiar "Internal Database URL"
3. Pegarla en Environment Variables del Web Service

---

**¿Prefieres trabajar solo en la nube?** → Ve directamente a `DEPLOYMENT.md`

