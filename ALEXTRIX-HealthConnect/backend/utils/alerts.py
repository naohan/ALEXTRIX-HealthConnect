from typing import Optional

def analizar_datos_criticos(frecuencia_cardiaca: float, spo2: float, skin_temp: Optional[float] = None) -> Optional[str]:
    """
    Analiza los datos del sensor y detecta valores críticos
    
    Args:
        frecuencia_cardiaca: Frecuencia cardíaca del usuario
        spo2: Nivel de oxigenación
        skin_temp: Temperatura de la piel (opcional)
    
    Returns:
        str: Mensaje de alerta si se detecta un valor crítico, None en caso contrario
    """
    alerta = None
    
    if frecuencia_cardiaca > 130:
        alerta = "⚠️ Estrés alto"
    elif spo2 < 93:
        alerta = "❗ Baja oxigenación"
    elif skin_temp and skin_temp > 38:
        alerta = "🔥 Posible golpe de calor"
    
    return alerta




