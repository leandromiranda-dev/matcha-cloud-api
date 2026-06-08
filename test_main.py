from fastapi.testclient import TestClient
from main import app

# Creamos un cliente de prueba que simulará peticiones a tu API sin necesidad de encender el servidor
client = TestClient(app)

# PRUEBA 1: Verificar que el servidor responde (Health Check)
def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"estado": "ok", "mensaje": "API del Matcha Club funcionando correctamente."}

# PRUEBA 2: Verificar predicción con clima normal (Validación de estructura de respuesta)
def test_prediccion_dia_normal():
    payload = {
        "dia_semana_num": 2, # Miércoles
        "es_fin_semana": 0,  # No
        "temperatura_max": 25.0
    }
    response = client.post("/predecir", json=payload)
    assert response.status_code == 200
    datos_respuesta = response.json()
    assert "cluster_matematico" in datos_respuesta
    assert "recomendacion_operativa" in datos_respuesta

# PRUEBA 3: Verificar que el modelo procesa decimales y fines de semana sin colapsar
def test_prediccion_calor_extremo():
    payload = {
        "dia_semana_num": 6, # Domingo
        "es_fin_semana": 1,  # Sí
        "temperatura_max": 38.5
    }
    response = client.post("/predecir", json=payload)
    assert response.status_code == 200
    # Aseguramos que la respuesta devuelva un número entero como cluster
    assert isinstance(response.json()["cluster_matematico"], int)