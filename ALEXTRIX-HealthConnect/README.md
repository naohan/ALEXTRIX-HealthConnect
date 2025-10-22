# ALEXTRIX HealthConnect - Backend API

API REST y WebSocket en tiempo real para monitoreo de datos fisiológicos enviados desde un smartwatch (Xiaomi Watch 2 con Wear OS).

## 🎯 Características

- **API REST con FastAPI**: Endpoints para recibir y consultar datos de sensores
- **WebSocket en Tiempo Real**: Transmisión instantánea de datos al dashboard
- **Base de Datos MySQL**: Almacenamiento persistente con SQLAlchemy
- **Sistema de Alertas**: Análisis automático de valores críticos
- **CORS Habilitado**: Permite conexión desde el dashboard web
- **Reconexión Automática**: Manejo robusto de conexiones de BD

## 📁 Estructura del Proyecto

```
ALEXTRIX-HealthConnect/
│
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias de Python
├── .env                    # Variables de entorno (crear manualmente)
├── datos.json             # Archivo de respaldo de datos
│
└── backend/
    ├── __init__.py
    ├── database.py         # Configuración de SQLAlchemy
    ├── models.py           # Modelos de base de datos
    │
    ├── routers/
    │   ├── __init__.py
    │   └── sensores.py     # Endpoints REST
    │
    └── utils/
        ├── __init__.py
        ├── alerts.py       # Sistema de detección de alertas
        └── websocket_manager.py  # Gestor de WebSocket
```

## 🚀 Instalación y Configuración

### 1. Instalar Dependencias

```bash
# Crear entorno virtual (opcional pero recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar Base de Datos

Crear archivo `.env` en la raíz del proyecto:

```env
DB_USER=root
DB_PASS=
DB_NAME=alextrix_db
DB_HOST=localhost
```

### 3. Iniciar MySQL

Asegúrate de tener MySQL ejecutándose (XAMPP, WAMP, o instalación local).

La base de datos `alextrix_db` se creará automáticamente al iniciar el servidor.

### 4. Ejecutar el Servidor

```bash
# Modo desarrollo (con recarga automática)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Modo producción
uvicorn main:app --host 0.0.0.0 --port 8000
```

El servidor estará disponible en:
- **API**: http://127.0.0.1:8000
- **Documentación**: http://127.0.0.1:8000/docs
- **WebSocket**: ws://127.0.0.1:8000/ws/datos

## 📡 Endpoints API

### GET /
Verificar estado del servidor
```json
{
  "message": "Servidor ALEXTRIX activo ✅",
  "version": "2.0"
}
```

### GET /api/sensores
Obtener últimos 50 registros

**Respuesta:**
```json
[
  {
    "idUsuario": "user123",
    "frecuenciaCardiaca": 72.0,
    "spo2": 98.0,
    "skinTemp": 36.5,
    "gps": {"lat": -16.3989, "lon": -71.537},
    "timestamp": "2025-10-20T10:30:00",
    "hora_recepcion": "2025-10-20T10:30:05"
  }
]
```

### GET /api/sensores/ultimo
Obtener último registro del sistema

### POST /api/sensores
Recibir datos del smartwatch

**Body:**
```json
{
  "idUsuario": "user123",
  "frecuenciaCardiaca": 75.0,
  "spo2": 98.0,
  "skinTemp": 36.5,
  "alerta": "Normal",
  "gps": {
    "lat": -16.3989,
    "lon": -71.537
  },
  "timestamp": "2025-10-20T10:30:00"
}
```

**Respuesta:**
```json
{
  "status": "ok",
  "mensaje": "Dato guardado correctamente",
  "alerta": "Normal"
}
```

## 🔌 WebSocket

### Endpoint: /ws/datos

Conexión WebSocket para recibir datos en tiempo real.

**Ejemplo de conexión (JavaScript):**
```javascript
const socket = new WebSocket("ws://127.0.0.1:8000/ws/datos");

socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log("Nuevo dato recibido:", data);
};
```

## ⚠️ Sistema de Alertas

El sistema analiza automáticamente los valores y genera alertas:

### Frecuencia Cardíaca
- **Normal**: 60-130 BPM
- **⚠️ Estrés alto**: >130 BPM

### SpO₂ (Saturación de Oxígeno)
- **Normal**: ≥93%
- **❗ Baja oxigenación**: <93%

### Temperatura Corporal
- **Normal**: <38°C
- **🔥 Posible golpe de calor**: >38°C

## 🗄️ Base de Datos

### Tabla: registros

| Campo             | Tipo        | Descripción                    |
|-------------------|-------------|--------------------------------|
| id                | Integer (PK)| ID autoincremental             |
| idUsuario         | String(50)  | Identificador del usuario      |
| frecuenciaCardiaca| Float       | Frecuencia cardíaca (BPM)      |
| spo2              | Float       | Saturación de oxígeno (%)      |
| skinTemp          | Float       | Temperatura de la piel (°C)    |
| lat               | Float       | Latitud GPS                    |
| lon               | Float       | Longitud GPS                   |
| timestamp         | String(50)  | Marca de tiempo del smartwatch |
| hora_recepcion    | DateTime    | Hora de recepción en servidor  |

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para gestión de base de datos
- **PyMySQL**: Driver de MySQL para Python
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **WebSocket**: Comunicación bidireccional en tiempo real
- **Python-dotenv**: Gestión de variables de entorno

## 🔒 Configuración CORS

El servidor permite conexiones desde cualquier origen para desarrollo.

Para producción, modifica en `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tu-dominio.com"],  # Especifica tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🧪 Pruebas

### Probar con curl

```bash
# Verificar estado
curl http://127.0.0.1:8000/

# Enviar datos
curl -X POST http://127.0.0.1:8000/api/sensores \
  -H "Content-Type: application/json" \
  -d '{
    "idUsuario": "test123",
    "frecuenciaCardiaca": 75,
    "spo2": 98,
    "skinTemp": 36.5,
    "gps": {"lat": -16.3989, "lon": -71.537},
    "timestamp": "2025-10-20T10:30:00"
  }'
```

### Documentación Interactiva

Accede a http://127.0.0.1:8000/docs para ver la documentación Swagger UI interactiva.

## 📞 Troubleshooting

### Error: "Can't connect to MySQL server"
- Verifica que MySQL esté ejecutándose
- Comprueba las credenciales en el archivo `.env`
- Asegúrate de que el puerto 3306 esté disponible

### Error: "WebSocket connection failed"
- Verifica que el servidor esté ejecutándose en el puerto 8000
- Comprueba que no haya firewall bloqueando la conexión
- Asegúrate de usar `ws://` y no `wss://` en desarrollo

### Error: "Module not found"
- Ejecuta `pip install -r requirements.txt`
- Verifica que el entorno virtual esté activado

## 🚀 Deploy en Render

### Configuración en Render.com

1. **Crear cuenta en Render.com**

2. **Crear Web Service:**
   - Conecta tu repositorio de GitHub
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Variables de entorno:**
   ```
   DB_USER=tu_usuario_mysql
   DB_PASS=tu_password_mysql
   DB_NAME=alextrix_db
   DB_HOST=tu_host_mysql
   ```

4. **Nota:** Necesitarás una base de datos MySQL externa (Render MySQL, Railway, o PlanetScale)

## 📞 Soporte

Proyecto desarrollado para **TECSUP Arequipa** como parte del sistema ALEXTRIX HealthConnect.

---

**© 2025 ALEXTRIX HealthConnect - TECSUP Arequipa**

