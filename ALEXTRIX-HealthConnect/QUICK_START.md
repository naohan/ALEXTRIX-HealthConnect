# 🚀 Inicio Rápido - ALEXTRIX HealthConnect

## ✅ El proyecto está listo para GitHub y Render

---

## 📦 OPCIÓN 1: Subir directo a GitHub → Render (RECOMENDADO)

### Paso 1: Subir a GitHub (5 min)

```powershell
# Ir al directorio del proyecto
cd "C:\Users\Tecsup\Documents\VI\IdeDatos\labs\ALERTRIX\ALEXTRIX-HealthConnect\ALEXTRIX-HealthConnect"

# Inicializar Git
git init
git add .
git commit -m "Initial commit: ALEXTRIX HealthConnect Backend API"

# Conectar con GitHub (reemplaza TU_USUARIO)
git remote add origin https://github.com/TU_USUARIO/ALEXTRIX-HealthConnect.git

# Subir
git branch -M main
git push -u origin main
```

### Paso 2: Deploy en Render (10 min)

1. **Crear PostgreSQL:**
   - Render.com → New + → PostgreSQL
   - Name: `alextrix-db`
   - Region: Oregon (Free)
   - Guarda el "Internal Database URL"

2. **Crear Web Service:**
   - New + → Web Service
   - Conecta tu repo GitHub
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Configurar DATABASE_URL:**
   - Environment → Add Environment Variable
   - Key: `DATABASE_URL`
   - Value: (pega el Internal Database URL de PostgreSQL)

4. **Deploy automático** ✨

Tu API estará en: `https://alextrix-healthconnect.onrender.com`

---

## 💻 OPCIÓN 2: Probar localmente primero

### Requisitos:
- PostgreSQL instalado
- Python 3.12+
- Virtualenv activado

### Pasos:

```powershell
# 1. Activar entorno virtual
cd "C:\Users\Tecsup\Documents\VI\IdeDatos\labs\ALERTRIX\ALEXTRIX-HealthConnect"
.\venv\Scripts\Activate.ps1

# 2. Entrar al directorio del proyecto
cd ALEXTRIX-HealthConnect

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear archivo .env
# (copia env.example y configura tus credenciales PostgreSQL)

# 5. Ejecutar servidor
uvicorn main:app --reload
```

Servidor en: http://127.0.0.1:8000

📖 **Ayuda con PostgreSQL local:** Lee `POSTGRESQL_SETUP.md`

---

## 📚 Guías Detalladas

- **`GITHUB_SETUP.md`** - Paso a paso para GitHub
- **`DEPLOYMENT.md`** - Paso a paso para Render
- **`POSTGRESQL_SETUP.md`** - Instalar PostgreSQL localmente
- **`README.md`** - Documentación completa

---

## ⚡ Cambios importantes (MySQL → PostgreSQL)

✅ Ya aplicados automáticamente:

- `requirements.txt` - Cambiado `pymysql` → `psycopg2-binary`
- `backend/database.py` - Soporta PostgreSQL
- `env.example` - Actualizado para PostgreSQL
- Documentación actualizada

**No necesitas hacer nada más** 🎉

---

## 🔍 Resolver error actual

El error que tienes ahora:
```
ERROR: Error loading ASGI app. Could not import module "main".
```

**Causa:** Estás en el directorio equivocado

**Solución:**
```powershell
cd ALEXTRIX-HealthConnect
uvicorn main:app --reload
```

Debes estar en:
```
C:\...\ALEXTRIX-HealthConnect\ALEXTRIX-HealthConnect\
```

No en:
```
C:\...\ALEXTRIX-HealthConnect\
```

---

## 🎯 Siguiente Paso Recomendado

1. **Sube a GitHub** (usa `GITHUB_SETUP.md`)
2. **Despliega en Render** (usa `DEPLOYMENT.md`)
3. **Actualiza el smartwatch** con la URL de Render

---

**¿Dudas?** Lee las guías detalladas en los archivos `.md` 📖

