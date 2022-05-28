import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import json



def app():
    #fig, ax = plt.subplots(figsize=(10, 10))
    #ax = sns.heatmap(dtf.pivot_table(index='Country', columns='Year', values='Score', aggfunc='sum', sort=False),
    #                 annot=True)
    #st.pyplot(fig)

    st.markdown(""" ## A Global View """)

    data = pd.read_csv('HDIp2.csv', encoding='latin-1')
    world = json.load(open("world_countries_geojson.geojson"))
    id_map = {}
    for feature in world['features']:
        feature['id'] = feature['properties']['cartodb_id']
        id_map[feature['properties']['name']] = feature['id']
    data['id'] = data['Country'].apply(lambda x: id_map[x])
    figg = px.choropleth(data, locations='id', geojson=world, color='HDI rank', hover_name='Country',
                         projection='natural earth')
    st.plotly_chart(figg)
    st.write('Clearly, Africa being the lightest region on the map is the least developed Continent and Europe being '
             'the darkest region on the map is the most developed Continent. ')
