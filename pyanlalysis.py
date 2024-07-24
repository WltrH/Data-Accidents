import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import plotly.express as px
import warnings
import folium as fo

#from streamlit_extras import dataframe_explorer
#from streamlit_extras.chart_container import chart_container

warnings.filterwarnings('ignore')


#Importation of AccidentUS.json
df = pd.read_json('/path/to/AccidentUS.json')

# Titre de l'application
st.title("Analyse scientifique avec Streamlit")

# Ajoutez votre code d'analyse scientifique ici



x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
st.pyplot(plt)

# Exemple : Afficher une table de données

data = {
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Âge': [25, 30, 35],
    'Ville': ['Paris', 'Londres', 'New York']
}

df = pd.DataFrame(data)

st.write(df)