import streamlit as st
import streamlit_extras as stx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import warnings

from streamlit_extras import dataframe_explorer
from streamlit_extras.chart_container import chart_container

warnings.filterwarnings('ignore')


#Importation of AccidentUS.json
df = pd.read_json('/path/to/AccidentUS.json')

# prise des données qui nous intéressent
colonnes = ['Crash Date/Time', 'Hit/Run', 'Route Type', 'Lane Direction',
    'Lane Type', 'Number of Lanes', 'Weather', 'Surface Condition', 'Light',
    'Traffic Control', 'Driver Substance Abuse',
    'Non-Motorist Substance Abuse', 'Collision Type', 'Related Non-Motorist',
    'At Fault', 'First Harmful Event', 'Second Harmful Event', 'Latitude',
    'Longitude', 'Location']
df = colonnes

# Affichage des données
st.write(df)

# Titre de l'application
st.title("Analyse scientifique avec Streamlit")

####################Setting######################
page_title = "Accident USA Data Analysis"
page_icon = ":bar_chart:"
layout = "centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# Container 1
with st.container():
    st.write("This is a container")
    st.write("Tentative d'analyse de données")

    #création d'un graphique histogramme sur le nombre d'accident par années
    #fig = px.histogram(df, x='Crash Date/Time', y=('ACRS Report Type'), title='Nombre d\'accidents par années')
    #st.plotly_chart(fig)

    #Création histogramme du nombre totale d'accident pas années
    fig = px.histogram(df, x='Crash Date/Time', y=('ACRS Report Type'), title='Nombre total d\'accidents par années')
    st.plotly_chart(fig)


    # Display the data frame
    st.write(df)

# Container 2

with st.container():

    st.write("Ceci est un container")
    st.write("Vous pouvez l'utiliser pour organiser votre contenu")


    m = fo.Map(location=[48.8566, 2.3522], zoom_start=12)
    st.map(m)

    # Afficher le data frame
    st.write(df)

 # Container 3
 
with st.container():
    st.write("This is a container")
    st.write("You can use it to organize your content")

    # Container 3
    with st.container():
        st.write("This is a container")
        st.write("You can use it to organize your content")

        # Create a bar chart using matplotlib
        fig, ax = plt.subplots()
        ax.bar(df['column_name'], df['column_name'])
        st.pyplot(fig)