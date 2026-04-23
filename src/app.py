#from utils import db_connect
#engine = db_connect()

# your code here
import streamlit as st
import pickle
import os

# 1. Construir la ruta absoluta de forma segura
# Esto ubica la carpeta actual (src) y luego sube a models
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../models/nba_model.sav')

# Cargar el modelo usando la ruta segura
modelo = pickle.load(open(MODEL_PATH, 'rb'))

# 2. Diccionario para traducir la predicción a texto legible
nombres_posiciones = {
    'G': 'Guard (Base / Escolta)',
    'F': 'Forward (Alero / Ala-Pívot)',
    'C': 'Center (Pívot)'
}

# 3. Título y descripción de la app web
st.title("Predictor de Posiciones NBA 🏀")
st.write("¿Qué posición jugarías según tus estadísticas?")

# 4. Crear los campos de entrada de datos numéricos
# Usamos number_input para permitir decimales (min_value evita valores negativos)
mpg = st.number_input("Minutos Jugados (MPG)", min_value=0.0, step=0.1)
tpa = st.number_input("Triples Intentados (3PA)", min_value=0.0, step=0.1)
tpp = st.number_input("Porcentaje Triples (3P%)", min_value=0.0, step=0.1)
ppg = st.number_input("Puntos por juego (PPG)", min_value=0.0, step=0.1)
rpg = st.number_input("Rebotes por juego (RPG)", min_value=0.0, step=0.1)
apg = st.number_input("Asistencias por juego (APG)", min_value=0.0, step=0.1)
spg = st.number_input("Robos por juego (SPG)", min_value=0.0, step=0.1)
bpg = st.number_input("Tapones por juego (BPG)", min_value=0.0, step=0.1)

# 5. Crear el botón que acciona la predicción
if st.button("Adivinar Posición"):
    
    # 6. Agrupar los datos ingresados en el MISMO ORDEN del entrenamiento
    datos_ingresados = [[mpg, tpa, tpp, ppg, rpg, apg, spg, bpg]]
    
    # 7. Ejecutar la predicción con el modelo
    resultado_crudo = modelo.predict(datos_ingresados)[0]
    prediccion = nombres_posiciones[resultado_crudo]
    
    # 8. Mostrar el resultado final con un cuadro de éxito (verde)
    st.success(f"¡El modelo dice que eres: {prediccion}!")