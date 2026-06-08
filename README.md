# 🍵 Matcha Club - Predictive Cloud API

Microservicio de Inteligencia Artificial desplegado en la nube para predecir la demanda operativa y emitir recomendaciones de gestión para el Matcha Club. 

Este proyecto implementa un modelo de Machine Learning (XGBoost) a través de una API RESTful, diseñado bajo una arquitectura tolerante a fallos con contenedores y pipelines de despliegue continuo (CI/CD).

## 🏗️ Arquitectura del Sistema

El sistema fue diseñado cumpliendo con los estándares de **Cloud Native** y automatización de infraestructura:

* **Pilar 1 - Contenedores y Orquestación:** La API está empaquetada en una imagen Docker optimizada (Multi-stage build) y orquestada mediante **Kubernetes (K3s)** en una instancia EC2 de AWS, garantizando alta disponibilidad a través de réplicas de pods y balanceo de carga.
* **Pilar 3 - Integración y Despliegue Continuo (CI/CD):** Pipeline automatizado con **GitHub Actions**. Ante cada cambio en la rama principal, el entorno en la nube ejecuta pruebas unitarias estrictas (`pytest`), construye la nueva imagen y la actualiza en el registro de Docker Hub sin intervención manual.

## 🛠️ Stack Tecnológico

* **Machine Learning:** Python, XGBoost, Pandas, Scikit-Learn.
* **Backend:** FastAPI, Uvicorn.
* **DevOps & Cloud:** Docker, Kubernetes (K3s), GitHub Actions, AWS (EC2).

## 🚀 Uso de la API (Endpoints)

La API expone una interfaz interactiva Swagger UI para realizar predicciones en tiempo real.

**Endpoint Principal:** `POST /predecir`

**Payload de ejemplo (JSON):**
{
  "dia_semana_num": 1,
  "es_fin_semana": 0,
  "temperatura_max": 20.0
}

**Respuesta de ejemplo:**
{
  "cluster_matematico": 2,
  "recomendacion_operativa": "Día Regular (Base) - Operación normal"
}

## 🧪 Ejecución de Pruebas Locales

Para ejecutar la batería de pruebas unitarias que validan la integridad del modelo y las respuestas del servidor:

1. Instalar dependencias de desarrollo: `pip install pytest httpx`
2. Ejecutar el entorno de pruebas: `python -m pytest`
