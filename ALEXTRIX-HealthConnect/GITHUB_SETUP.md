# 📦 Guía Rápida: Subir a GitHub

## 🔧 Comandos paso a paso

### 1️⃣ Inicializar repositorio Git

```powershell
cd "C:\Users\Tecsup\Documents\VI\IdeDatos\labs\ALERTRIX\ALEXTRIX-HealthConnect\ALEXTRIX-HealthConnect"

git init
```

### 2️⃣ Configurar usuario Git (si es primera vez)

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### 3️⃣ Agregar archivos al staging

```powershell
git add .
```

### 4️⃣ Hacer el primer commit

```powershell
git commit -m "Initial commit: ALEXTRIX HealthConnect Backend API"
```

### 5️⃣ Crear repositorio en GitHub

1. Ve a: https://github.com/new
2. Nombre: `ALEXTRIX-HealthConnect`
3. Descripción: `Backend API para monitoreo de salud con smartwatch`
4. Visibilidad: **Public** o **Private**
5. **NO marques** "Initialize with README"
6. Click "Create repository"

### 6️⃣ Conectar con GitHub

```powershell
# Reemplaza TU_USUARIO con tu usuario de GitHub
git remote add origin https://github.com/TU_USUARIO/ALEXTRIX-HealthConnect.git

# Verificar
git remote -v
```

### 7️⃣ Subir a GitHub

```powershell
git branch -M main
git push -u origin main
```

Si te pide credenciales:
- **Username:** tu usuario de GitHub
- **Password:** usa un **Personal Access Token** (no tu contraseña)

#### Crear Personal Access Token:
1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token
4. Marca: `repo` (Full control)
5. Copia el token (lo usarás como password)

---

## ✅ Verificar

Ve a tu repositorio en GitHub:
```
https://github.com/TU_USUARIO/ALEXTRIX-HealthConnect
```

Deberías ver todos tus archivos excepto:
- ❌ `venv/` (ignorado)
- ❌ `__pycache__/` (ignorado)
- ❌ `.env` (ignorado - **NUNCA subir credenciales**)
- ✅ `requirements.txt`
- ✅ `main.py`
- ✅ `backend/`
- ✅ `README.md`
- ✅ `Procfile`

---

## 🔄 Actualizar el repositorio después de cambios

```powershell
# Ver cambios
git status

# Agregar cambios
git add .

# Guardar cambios
git commit -m "Descripción de los cambios"

# Subir a GitHub
git push
```

---

## 🚀 Siguiente paso: Deploy en Render

Lee el archivo `DEPLOYMENT.md` para instrucciones de deployment en Render.com

