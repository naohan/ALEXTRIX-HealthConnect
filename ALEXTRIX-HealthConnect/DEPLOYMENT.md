# 🚀 Guía de Deployment - ALEXTRIX HealthConnect

## 📋 Checklist antes de subir a GitHub

- [x] `.gitignore` creado
- [x] `requirements.txt` actualizado
- [x] `Procfile` para deployment
- [x] `runtime.txt` con versión de Python
- [ ] `.env.example` (NO subir `.env` real)
- [x] README.md actualizado

---

## 🔧 PASO 1: Preparar el repositorio local

### 1.1 Inicializar Git

```bash
cd ALEXTRIX-HealthConnect
git init
git add .
git commit -m "Initial commit: ALEXTRIX HealthConnect API"
```

### 1.2 Crear archivo .env local (NO subir a GitHub)

Crea un archivo `.env` con tus credenciales locales:
```env
DB_USER=root
DB_PASS=
DB_NAME=alextrix_db
DB_HOST=localhost
```

⚠️ **IMPORTANTE:** Este archivo NO se subirá a GitHub (está en `.gitignore`)

---

## 📤 PASO 2: Subir a GitHub

### 2.1 Crear repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre del repositorio: `ALEXTRIX-HealthConnect`
3. **NO** inicialices con README (ya lo tienes)
4. Click en "Create repository"

### 2.2 Conectar y subir

```bash
# Agregar el repositorio remoto (reemplaza TU_USUARIO)
git remote add origin https://github.com/TU_USUARIO/ALEXTRIX-HealthConnect.git

# Verificar
git remote -v

# Subir al repositorio
git branch -M main
git push -u origin main
```

---

## 🌐 PASO 3: Deploy en Render

### 3.1 Crear cuenta en Render

1. Ve a https://render.com
2. Regístrate con GitHub (recomendado)
3. Autoriza acceso a tus repositorios

### 3.2 Crear Base de Datos MySQL

**Opción A: Render MySQL (Recomendado)**

1. En Render Dashboard → Click "New +"
2. Selecciona "MySQL"
3. Configuración:
   - **Name:** `alextrix-db`
   - **Database:** `alextrix_db`
   - **User:** (se genera automático)
   - **Region:** Oregon (Free tier)
4. Click "Create Database"
5. **Guarda las credenciales:**
   - Internal Database URL
   - Host
   - Username
   - Password

**Opción B: Railway (Alternativa gratuita)**

1. Ve a https://railway.app
2. New Project → Provision MySQL
3. Copia las credenciales

**Opción C: PlanetScale (MySQL serverless)**

1. Ve a https://planetscale.com
2. Create database → Free tier
3. Obtén connection string

### 3.3 Crear Web Service

1. En Render Dashboard → Click "New +"
2. Selecciona "Web Service"
3. Conecta tu repositorio `ALEXTRIX-HealthConnect`
4. Configuración:

```
Name: alextrix-healthconnect
Region: Oregon (Free)
Branch: main
Root Directory: ALEXTRIX-HealthConnect
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
Instance Type: Free
```

### 3.4 Configurar Variables de Entorno

En el panel de Render, ve a "Environment" y agrega:

```
DB_USER=tu_usuario_render_mysql
DB_PASS=tu_password_render_mysql
DB_NAME=alextrix_db
DB_HOST=tu_host_render_mysql (ej: dpg-xxxxx-a.oregon-postgres.render.com)
```

⚠️ **Usa las credenciales de la base de datos que creaste en 3.2**

### 3.5 Deployar

1. Click "Create Web Service"
2. Render automáticamente:
   - Clona tu repositorio
   - Instala dependencias
   - Ejecuta el servidor
3. Espera 2-5 minutos

### 3.6 Obtener URL

Tu API estará disponible en:
```
https://alextrix-healthconnect.onrender.com
```

**Endpoints:**
- API Docs: https://alextrix-healthconnect.onrender.com/docs
- WebSocket: wss://alextrix-healthconnect.onrender.com/ws/datos

---

## ✅ PASO 4: Verificar Deployment

### 4.1 Probar el servidor

```bash
# Verificar que el servidor esté activo
curl https://alextrix-healthconnect.onrender.com/

# Debe retornar:
# {"message":"Servidor ALEXTRIX activo ✅","version":"2.0"}
```

### 4.2 Probar API Docs

Abre en tu navegador:
```
https://alextrix-healthconnect.onrender.com/docs
```

### 4.3 Probar POST desde el smartwatch

Actualiza la URL en tu app de Wear OS:
```kotlin
// Antes (desarrollo local)
val BASE_URL = "http://192.168.1.X:8000"

// Después (producción)
val BASE_URL = "https://alextrix-healthconnect.onrender.com"
```

---

## 🔄 PASO 5: Actualizar el proyecto

Cuando hagas cambios en el código:

```bash
# 1. Hacer cambios en tu código local
# 2. Guardar cambios en Git
git add .
git commit -m "Descripción de los cambios"
git push origin main

# 3. Render detecta automáticamente y redeploya
```

---

## 🐛 Troubleshooting

### Error: "Application failed to respond"
- Verifica las variables de entorno en Render
- Revisa los logs: Render Dashboard → Logs
- Asegúrate de que MySQL esté activo

### Error: "Can't connect to MySQL"
- Verifica las credenciales de la base de datos
- Usa el "Internal Database URL" de Render (más rápido)
- Verifica que el puerto sea el correcto

### WebSocket no conecta
- Usa `wss://` en lugar de `ws://` en producción
- Verifica CORS en `main.py`

### El deploy es lento
- Render Free tier entra en "sleep" después de 15 min de inactividad
- La primera petición puede tardar 30-60 segundos
- Considera upgrade a plan pagado para evitar sleep

---

## 💡 Mejoras para Producción

### 1. Usar Base de Datos en la nube

**PlanetScale (Recomendado):**
- 10GB gratis
- MySQL serverless
- Sin sleep mode
- https://planetscale.com

**Railway:**
- $5 gratis al mes
- MySQL + PostgreSQL
- https://railway.app

### 2. Agregar dominio personalizado

En Render:
1. Settings → Custom Domain
2. Agregar: `api.alextrix.com`
3. Configurar DNS

### 3. Monitoreo

- Render incluye logs básicos
- Considera: Sentry, LogRocket, o New Relic

### 4. CI/CD Automático

Ya está configurado automáticamente con GitHub → Render

---

## 📞 Recursos Útiles

- **Render Docs:** https://render.com/docs
- **FastAPI Deployment:** https://fastapi.tiangolo.com/deployment/
- **MySQL en Render:** https://render.com/docs/databases

---

**¡Listo! Tu API está en producción 🚀**

