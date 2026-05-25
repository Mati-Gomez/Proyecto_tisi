import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración inicial de la página
st.set_page_config(
    page_title="Investigación de Mercado UNLP", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inyección de CSS global para Streamlit (Montserrat y fondo blanco)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif !important;
        background-color: #FFFFFF !important;
    }
    
    /* Estilizar los tabs nativos de Streamlit para que sean minimalistas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: #666666;
        font-family: 'Montserrat', sans-serif;
    }
    .stTabs [aria-selected="true"] {
        color: #7C3AED !important; /* Lila principal */
        border-bottom-color: #7C3AED !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Análisis de Mercado: Micro-servicios UNLP")

# 3. Motor de limpieza y adaptación del HTML
def procesar_html(html_str):
    if not html_str:
        return ""

    # A. Eliminar emojis explícitos
    emojis = ['⚡', '🔥', '🚿', '❄️', '🎨', '⭐', '★']
    for e in emojis:
        html_str = html_str.replace(e, '')
    
    # B. Inyectar variables CSS para forzar la fuente y la paleta lila en el HTML incrustado
    css_inyection = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
    * { font-family: 'Montserrat', sans-serif !important; }
    :root {
        --color-text-primary: #1F2937;
        --color-text-secondary: #4B5563;
        --color-text-tertiary: #9CA3AF;
        --color-background-primary: #FFFFFF;
        --color-background-secondary: #F3F4F6; /* Gris muy claro para tarjetas */
        --color-border-tertiary: #E5E7EB;
        --color-background-info: #F3E8FF; /* Fondo lila claro para alertas */
        --color-text-info: #6B21A8; /* Texto púrpura */
    }
    </style>
    """
    html_str = css_inyection + html_str

    # C. Reemplazar los colores duros originales por una escala monocromática/lila
    reemplazos_color = {
        '#3266ad': '#7C3AED', # Púrpura principal (Eléctrica)
        '#1d9e75': '#8B5CF6', # Púrpura secundario (Sanitaria)
        '#d85a30': '#A78BFA', # Lila medio (Aire Acondicionado)
        '#ba7517': '#C4B5FD', # Lila claro (Gas)
        '#888780': '#DDD6FE', # Lila muy claro (Pinturas)
        '#5580c0': '#8B5CF6', # Variaciones para el mapa de calor
        '#1a5fa0': '#6D28D9',
        '#0a3060': '#4C1D95'
    }
    for original, nuevo in reemplazos_color.items():
        html_str = html_str.replace(original, nuevo)

    return html_str

# 4. Función de carga de archivos locales
def load_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"<p style='color:red;'>Error: No se encontró el archivo <b>{filename}</b> en el directorio.</p>"

# Cargar y procesar los 3 archivos
html_investigacion = procesar_html(load_file('investigacionUNLP.txt'))
html_estacionalidad = procesar_html(load_file('estacionalidad.txt'))
html_ticket = procesar_html(load_file('ticketpromedio.txt'))

# 5. Estructura de Pestañas (Secciones)
tab1, tab2, tab3 = st.tabs(["Contexto y Demanda", "Estacionalidad y Calendario", "Ticket Promedio"])

with tab1:
    components.html(html_investigacion, height=900, scrolling=True)

with tab2:
    components.html(html_estacionalidad, height=900, scrolling=True)

with tab3:
    components.html(html_ticket, height=900, scrolling=True)
