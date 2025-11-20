import streamlit as st 
import pandas as pd
from utils.data_loader import load_project_data

st.title("Analisis de proyectos")

df= load_project_data()

with st.sidebar:
    st.markdown("### Filtros proyectos")

    estados= df['State'].dropna().unique().tolist()
    estado_filtro = st.multiselect("Region", estados, default=estados)

    areas = df['Geographical scope'].dropna().unique().tolist()
    area_filtro = st.selectbox("Area geografico", ["Todos"] + areas)

    avance_min = st.slider("Avance mínimo (%)", 0, 100, 0)