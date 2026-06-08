# 🍵 Matcha Club - Cloud AI Predictor

Microservicio de Inteligencia Artificial Full-Stack desplegado en la nube para predecir la demanda operativa y emitir recomendaciones de gestión para el Matcha Club. 

Este proyecto evoluciona de una API RESTful tradicional a una solución web interactiva, respaldada por un modelo predictivo de Machine Learning (XGBoost) y operando sobre una arquitectura Cloud Native tolerante a fallos.

## 🏗️ Arquitectura del Sistema (Cloud Native)

El despliegue está diseñado bajo estrictos estándares de la industria, garantizando alta disponibilidad y actualizaciones continuas sin tiempo de inactividad (Rolling Updates):

* **Capa de Infraestructura (AWS):** Aprovisionamiento sobre una instancia EC2 (`t3.medium`) operando como servidor dedicado.
* **Orquestación (Kubernetes):** Uso de **K3s** para gestionar el balanceo de carga (`LoadBalancer`) y mantener múltiples réplicas activas de los contenedores para prevenir caídas del servicio.
* **CI/CD Automatizado:** Pipeline integrado con **GitHub Actions** que ejecuta pruebas unitarias automatizadas (`pytest`), construye una imagen Docker optimizada (Multi-stage) y actualiza de forma invisible el registro en Docker Hub ante cada nuevo cambio en el código.

## 🛠️ Stack Tecnológico

* **Machine Learning:** Python 3.10, XGBoost, Pandas, Scikit-Learn.
* **Backend y Web:** FastAPI, Uvicorn, Pydantic, HTML5, Vanilla JavaScript.
* **DevOps y Nube:** Docker, Kubernetes (K3s), GitHub Actions, AWS EC2.

## 📁 Estructura del Repositorio

* `main.py`: Cerebro del backend (FastAPI) y enrutador web.
* `index.html`: Interfaz gráfica (Frontend) responsiva para la interacción comercial.
* `modelo_xgb.pkl`: Modelo matemático pre-entrenado.
* `Dockerfile`: Receta estricta para empaquetar el código, dependencias y archivos estáticos.
* `api-deployment.yaml`: Planos (Manifests) declarativos para levantar la infraestructura en Kubernetes.
* `.github/workflows/ci-cd.yml`: Instrucciones de automatización para el robot de integración continua.

## 🚀 Acceso y Uso

El clúster expone la aplicación unificando la vista comercial y la técnica en el mismo puerto:

1. **Interfaz Comercial:** Accediendo a la ruta principal (`http://<IP_PUBLICA>:8000/`), el sistema sirve el cliente web interactivo para que el personal del establecimiento obtenga predicciones de demanda basadas en el clima.
2. **Documentación Técnica:** Accediendo a `/docs` (`http://<IP_PUBLICA>:8000/docs`), se levanta la consola interactiva Swagger UI / OpenAPI para la integración formal de la API con otros sistemas.

## 🛡️ Estándares de Seguridad

Aplicando el principio de **Zero Trust**, este repositorio cumple con normativas de seguridad en la nube al no exponer claves privadas en el código fuente (Hardcoding). Las credenciales críticas para el pipeline de distribución se inyectan dinámicamente mediante **GitHub Secrets**, protegiendo la integridad de la infraestructura de AWS y Docker Hub.
