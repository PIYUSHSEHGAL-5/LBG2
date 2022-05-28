import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

dala = pd.read_csv('Env2.CSV',encoding='Latin')


def app():
    st.markdown(""" ## Forest Distribution (% of total land area) Across the World """)
    st.image("oiy.PNG")
    st.markdown(""" ## %Fossil fuel Energy Consumption""")
    clist = dala['Country'].tolist()
    clist.sort()
    s_c = st.selectbox('Select a country', clist)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax = plt.pie(dala[dala['Country'] == s_c].squeeze().tolist()[1:3], labels=['Fossil Fuel', ''], wedgeprops=
    {'edgecolor': 'black'},autopct='%1.1f%%', explode = [0.1,0],shadow=True,colors=['#696969','#228B22'])
    st.pyplot(fig)

