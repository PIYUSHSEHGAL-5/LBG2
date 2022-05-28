import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import json


data = pd.read_csv('HDIp2.csv', encoding='latin-1')


def app():
    st.title('Human Development Index')
    st.markdown(""" _The HDI was created to emphasize that people and their capabilities should be the ultimate criteria
     for assessing the development of a country, not economic growth alone. The HDI can also be used to question 
     national policy choices, asking how two countries with the same level of GNI per capita can end up with different 
     human development outcomes. These contrasts can stimulate debate about government policy priorities._""")
    st.markdown(""" ## Top 20 Countries according to 2019 Rankings """)
    st.table(data.head(20).rename(columns={'2019': 'Score'}).iloc[:,:3])
    st.markdown(""" ## Top 20 Countries according to 2019 Rankings """)
    st.table(data.tail(20).rename(columns={'2019': 'Score'}).iloc[:, :3])
    st.markdown(""" ## HDI Scores of Best and Worst Performing Countries from 1990-2019 """)

    st.image("tmp.png")










