from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.responses import FileResponse

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="Matcha Club - API Predictiva",
    description="API para predecir la demanda operativa basada en ML",
    version="1.0.0"
)

# Cargamos el modelo XGBoost pre-entrenado al iniciar el servidor
modelo = joblib.load('modelo_xgb.pkl')

# Definimos el formato estricto de los datos de entrada
class DatosClima(BaseModel):
    dia_semana_num: int      # 0 (Lunes) a 6 (Domingo)
    es_fin_semana: int       # 0 (No) o 1 (Sí)
    temperatura_max: float   # Grados centígrados (ej. 35.5)

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/predecir")
def predecir_demanda(datos: DatosClima):
    # 1. Convertimos el JSON recibido a un DataFrame de Pandas
    df_entrada = pd.DataFrame([{
        'Dia_Semana_Num': datos.dia_semana_num,
        'Es_Fin_Semana': datos.es_fin_semana,
        'Temperatura_Max': datos.temperatura_max
    }])
    
    # 2. El modelo XGBoost realiza la predicción
    prediccion_cluster = modelo.predict(df_entrada)[0]
    
    # 3. Traducción para el negocio
    diccionario_clusters = {
        0: "Día Valle (Baja Demanda) - Minimizar stock fresco",
        1: "Día Pico (Alta Demanda) - Alerta de calor, preparar Cold Drinks",
        2: "Día Regular (Base) - Operación normal"
    }
    
    # 4. Retornamos la respuesta al cliente
    return {
        "cluster_matematico": int(prediccion_cluster),
        "recomendacion_operativa": diccionario_clusters.get(int(prediccion_cluster), "Desconocido")
    }