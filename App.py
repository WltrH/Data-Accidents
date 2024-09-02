#importation des modules streamlit et pandas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import folium as fo




#Tittle of the application
st.title("Application de visualisation de données")

with st.container():
    st.write("Bienvenue sur notre application de visualisation de données")
    st.write("Cette application permet de visualiser les données des accidents de la route du Maryland")


with st.container():
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
    st.subheader("Nombre d'accidents par Années")
    #DataSet creation
    data['Crash Date/Time'] = pd.to_datetime(data['Crash Date/Time'])
    #bar chart of number of accidents by years
    fig = st.bar_chart(data['Crash Date/Time'].dt.year.value_counts())

    
st.markdown('---')

#Title
st.subheader("Veuillez choisir l'année, le mois et le jour pour visualiser les données")
#Select the year
option = st.selectbox(
    "Quelle année souhaitez vous sélèctionner?",
    ("2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024")
)


with st.container():
    #Title
    st.subheader("Nombre d'accidents pour l'année: " + option)
   
    #bar chart of number of accidents by years with the year selected in the selectbox
    fig = st.bar_chart(data[data['Crash Date/Time'].dt.year == int(option)]['Crash Date/Time'].dt.month.value_counts())

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
    fig1.patch.set_facecolor('white')

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
    st.subheader("Nombre de ype de collision total")
    #Name in lowercase
    data['Collision Type'] = data['Collision Type'].str.lower()
    #bar chart of number of accidents by collision type
    fig2 = st.bar_chart(data['Collision Type'].value_counts())

st.markdown('---')

with st.container():
    #Title
    st.subheader("Carte de chaleur des accidents par localisation")
    #heat map of accidents by years selected in option and location using folium
    accidents = data[data['Crash Date/Time'].dt.year == int(option)]
    accidents = accidents[['lat', 'lon']]
    accidents = accidents.dropna()
    accidents = accidents.values.tolist()
    map = fo.Map(location=[39.045753, -76.641273], zoom_start=10)
    fo.plugins.HeatMap(accidents).add_to(map)
    st.write(map)
