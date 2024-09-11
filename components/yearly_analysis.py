import streamlit as st
import pandas as pd
import plotly.express as px

def show_yearly_analysis(data):
    st.markdown("---")
    
    st.subheader("📊 Analyse Annuelle des Accidents")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Graphique des accidents par année
        yearly_data = data['Crash Date/Time'].dt.year.value_counts().sort_index()
        fig = px.bar(x=yearly_data.index, y=yearly_data.values,
                     labels={'x': 'Année', 'y': "Nombre d'accidents"},
                     title="Évolution du nombre d'accidents par année")
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Sélection de l'année
        st.subheader("Analyse mensuelle par année")
        option = st.selectbox(
            "Sélectionnez une année :",
            sorted(data['Crash Date/Time'].dt.year.unique(), reverse=True)
        )
        
        # Graphique des accidents par mois pour l'année sélectionnée
        monthly_data = data[data['Crash Date/Time'].dt.year == int(option)]['Crash Date/Time'].dt.month.value_counts().sort_index()
        month_names = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc']
        fig = px.bar(x=month_names, y=monthly_data.values,
                     labels={'x': 'Mois', 'y': "Nombre d'accidents"},
                     title=f"Répartition mensuelle des accidents en {option}")
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Métriques
    col1, col2, col3 = st.columns(3)
    col1.metric("Total d'accidents", f"{len(data):,}")
    col2.metric("Année avec le plus d'accidents", f"{yearly_data.idxmax()} ({yearly_data.max():,})")
    col3.metric("Moyenne annuelle", f"{yearly_data.mean():.0f}")

    st.markdown("---")