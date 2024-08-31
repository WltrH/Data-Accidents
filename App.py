#importation des modules streamlit et pandas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#Tittle of the application
st.title("Application de visualisation de données")

with st.container():
    st.write("Bienvenue sur notre application de visualisation de données")
    st.write("Cette application permet de visualiser les données des accidents de la route du Maryland")
    st.write("Vous pouvez visualiser les données ci-dessous")

#Download the CSV file Crash_Reporting_-_Incidents_Data.csv
data = pd.read_csv("Crash_Reporting_-_Incidents_Data.csv")

#Drop some columns
data = data.drop(columns=["Lane Type", "Off-Road Description", "Municipality", "Related Non-Motorist", "Non-Motorist Substance Abuse", "Second Harmful Event", "Intersection Type"])

#Display the data
st.write(data)
st.markdown('---')

with st.container():
    #Title
    st.subheader("Nombre d'accidents par année")
    #DataSet creation
    data['Crash Date/Time'] = pd.to_datetime(data['Crash Date/Time'])
    #bar chart of number of accidents by years
    fig = st.bar_chart(data['Crash Date/Time'].dt.year.value_counts())
   
    
st.markdown('---')

with st.container():
    #Title
    st.subheader("Pourcentage d'accidents par type de crash")

    #explode the first slice
    explode = (0.1, 0, 0)

    #Pie chart of percentage of accidents by crash type ACRS Report Type
    fig1, ax1 = plt.subplots()
    ax1.pie(data['ACRS Report Type'].value_counts(), explode= explode, labels=data['ACRS Report Type'].value_counts().index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    #background color of the pie chart transparent
    fig1.patch.set_facecolor('none')

    #Display the pie chart
    st.pyplot(fig1)
 
st.markdown('---')

with st.container():

    #Title
    st.subheader("Carte des accidents par localisation")

    #DataSet creation with the latitude and longitude columns and colision type
    data = data[['Latitude', 'Longitude', 'Collision Type']]
    #rename the columns Latitude and Longitude
    data = data.rename(columns={"Latitude": "lat", "Longitude": "lon"})
    #Heat map of accidents by location
    st.map(data)

st.markdown('---')

with st.container():
    #Title
    st.subheader("Carte de chaleur des accidents par type de collision")
    #bar chart of number of accidents by collision type
    fig2 = st.bar_chart(data['Collision Type'].value_counts())

st.markdown('---')

with st.container():
    #Title
    st.subheader("Nombre d'accidents par type de collision")
    #Heat map of accidents by collision type
    sns.heatmap(data['Collision Type'].value_counts().unstack(), annot=True, fmt="d")
    plt.show()
    st.pyplot()

st.markdown('---')

with st.container():
    #Title
    st.subheader("Nombre d'accidents par type de collision et par année")
    #Heat map of accidents by collision type and year
    sns.heatmap(data.groupby([data['Crash Date/Time'].dt.year, 'Collision Type']).size().unstack(), annot=True, fmt="d")
    plt.show()
    st.pyplot()