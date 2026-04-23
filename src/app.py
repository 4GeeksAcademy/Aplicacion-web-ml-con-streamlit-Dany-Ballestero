#from utils import db_connect
#engine = db_connect()

# your code here
import streamlit as st
import pickle
import os

# 1. Configuración de la página
st.set_page_config(page_title="Predictor NBA", layout="centered")

# 2. Construir la ruta absoluta de forma segura
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Intentamos detectar el nombre correcto del archivo (con o sin 's')
MODEL_PATH = os.path.join(BASE_DIR, '../models/nba_models.sav')
if not os.path.exists(MODEL_PATH):
    MODEL_PATH = os.path.join(BASE_DIR, '../models/nba_model.sav')

# 3. Cargar el modelo con manejo de errores
try:
    with open(MODEL_PATH, 'rb') as f:
        modelo = pickle.load(f)
except Exception as e:
    st.error(f"Error crítico al cargar el modelo: {e}")
    st.stop() # Detiene la ejecución si no hay modelo

# 4. Diccionario de posiciones
nombres_posiciones = {
    'G': 'Guard (Base / Escolta)',
    'F': 'Forward (Alero / Ala-Pívot)',
    'C': 'Center (Pívot)'
}

# 5. Interfaz de usuario
st.title("Predictor de Posiciones NBA 🏀")
st.write("Ingresa las estadísticas para predecir la posición del jugador.")

# Campos de entrada
mpg = st.number_input("Minutos Jugados (MPG)", min_value=0.0, step=0.1)
tpa = st.number_input("Triples Intentados (3PA)", min_value=0.0, step=0.1)
tpp = st.number_input("Porcentaje Triples (3P%)", min_value=0.0, step=0.1)
ppg = st.number_input("Puntos por juego (PPG)", min_value=0.0, step=0.1)
rpg = st.number_input("Rebotes por juego (RPG)", min_value=0.0, step=0.1)
apg = st.number_input("Asistencias por juego (APG)", min_value=0.0, step=0.1)
spg = st.number_input("Robos por juego (SPG)", min_value=0.0, step=0.1)
bpg = st.number_input("Tapones por juego (BPG)", min_value=0.0, step=0.1)

# 6. Botón de predicción
if st.button("Adivinar Posición"):
    datos_ingresados = [[mpg, tpa, tpp, ppg, rpg, apg, spg, bpg]]
    resultado_crudo = modelo.predict(datos_ingresados)[0]
    prediccion = nombres_posiciones.get(resultado_crudo, "Posición desconocida")
    
    st.success(f"¡El modelo dice que eres: {prediccion}!")