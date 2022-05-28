import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dyu = pd.read_csv('Pop2.csv',encoding='Latin')

def app():
    st.markdown(""" ## Average Annual Growth Rate of Best and Worst performing countries""")
    st.image("yo.jpg", width= 600)
    st.markdown(""" ## Total Fertility Rate of Best and Worst performing countries""")
    st.image("download.png", width=600)
    st.markdown(""" ## Mortality Rates Across Ages""")
    colist = dyu['Country'].tolist()
    colist.sort()
    selected_c = st.selectbox('Select a Country',colist)
    st.table(dyu[dyu['Country']==selected_c].iloc[:,1:].astype('int64'))
    st.write('Numbers displayed in each column are deaths per 1,000 people belonging to that category ')




