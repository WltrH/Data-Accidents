#importation des modules streamlit et pandas
import streamlit as st
from bokeh.plotting import figure
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px




#Tittle of the application
st.title("Application de visualisation de données")

with st.container():
    st.write("Bienvenue sur notre application de visualisation de données")
    st.write("Cette application permet de visualiser les données des accidents de la route du Maryland")

    #Download the CSV file Crash_Reporting_-_Incidents_Data.csv
    data = pd.read_csv("Crash_Reporting_-_Incidents_Data.csv")
with st.container():
    st.write("Vous pouvez visualiser les données ci-dessous")



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
    st.subheader("Nombre de Type de collision")
    #Name in lowercase
    data['Collision Type'] = data['Collision Type'].str.lower()
    #bar chart of number of accidents by collision type
    fig2 = st.bar_chart(data['Collision Type'].value_counts())

st.markdown('---')

with st.container():

    #title
    st.subheader("Nombre d'accidents par mois et par Années")
    #Download the CSV file Crash_Reporting_-_Incidents_Data.csv
    dacc = pd.read_csv("Crash_Reporting_-_Incidents_Data.csv")
    #keep columns crash date/time and collision type and drop the others
    dacc = dacc[['Crash Date/Time', 'ACRS Report Type']]
    #New column counting the number of accidents
    dacc['count'] = 1
    #Columns with the month
    dacc['Month'] = 0
    #Separation of the month from the date and push in the column Month
    for i in range(len(dacc)):
        dacc['Month'][i] = dacc['Crash Date/Time'][i].split('/')[0]
    #keep just the year in the column Crash Date/Time
    dacc['Crash Date/Time'] = dacc['Crash Date/Time'].str.split('/').str[2]
    #delete the hours in the column Crash Date/Time
    dacc['Crash Date/Time'] = dacc['Crash Date/Time'].str.split().str[0]
    #Group by year and month
    dacc = dacc.groupby(['Crash Date/Time', 'Month']).sum()
    #delete the colonne ARCS Report Type
    dacc = dacc.drop(columns=['ACRS Report Type'])
    #reset the index
    dacc = dacc.reset_index()
    #Group by year and month
    dacc = dacc.groupby(['Crash Date/Time', 'Month']).sum()
    #reset the index
    dacc = dacc.reset_index()
    #Display the data   
    #st.write(dacc)

    #test scatter plot
    fig3 = px.scatter(dacc, x="Month", y="count", color="Crash Date/Time")
    st.plotly_chart(fig3)


with st.container():
    #Different way to display the data
    #Download the CSV file Crash_Reporting_-_Incidents_Data.csv
    dataAcc = pd.read_csv("Crash_Reporting_-_Incidents_Data.csv")
    #Drop some columns
    dataAcc = dataAcc.drop(columns=["Lane Type", "Off-Road Description", "Municipality", "Related Non-Motorist", "Non-Motorist Substance Abuse", "Second Harmful Event", "Intersection Type"])
    #DataSet creation
    dataAcc['Crash Date/Time'] = pd.to_datetime(dataAcc['Crash Date/Time'])
    #Group by year and month
    dataAcc = dataAcc.groupby([dataAcc['Crash Date/Time'].dt.year, dataAcc['Crash Date/Time'].dt.month]).size().unstack()
    #index
    dataAcc.index = dataAcc.index.astype(str)
    #columns
    dataAcc.columns = dataAcc.columns.astype(str)
    #Fill the missing values with 0
    dataAcc = dataAcc.fillna(0)
    #creation new column of index
    dataAcc['index'] = dataAcc.index
    #reset the index
    dataAcc = dataAcc.reset_index(drop=True)
    #set the index
    dataAcc = dataAcc.set_index('index')
    #Title
    st.subheader("Tableau des accidents par Années et par Mois")
    #Display the data
    st.write(dataAcc)


st.markdown('---')

with st.container():

    #Title
    