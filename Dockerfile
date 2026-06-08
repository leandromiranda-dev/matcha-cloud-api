# ==========================================
# ETAPA 1: CONSTRUCTOR (Builder)
# ==========================================
FROM python:3.10-slim as builder

WORKDIR /build

# Copiamos solo el archivo de requerimientos primero (Aprovecha la caché de Docker)
COPY requirements.txt .

# Compilamos las dependencias en formato "wheel" para no arrastrar basura de instalación
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt


# ==========================================
# ETAPA 2: PRODUCCIÓN (Runner)
# ==========================================
FROM python:3.10-slim

WORKDIR /app

# Copiamos los paquetes ya compilados desde la Etapa 1
COPY --from=builder /build/wheels /wheels
COPY --from=builder /build/requirements.txt .

# Instalamos los paquetes limpios
RUN pip install --no-cache /wheels/*

# Copiamos el servidor y el cerebro de la IA
COPY main.py .
COPY modelo_xgb.pkl .

# Abrimos el puerto que usará FastAPI
EXPOSE 8000

# Comando inyectado para encender el servidor al iniciar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]