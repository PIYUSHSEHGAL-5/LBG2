import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

dama = pd.read_csv('GE2.CSV',encoding='Latin')
def app():
    st.markdown(""" ## Average Annual Growth Rate of Best and Worst performing countries""")
    st.image("sp.PNG", width=600)
    st.markdown(""" ## Share of Seats in Parliament held by women""")
    clist= dama['Country'].tolist()
    clist.sort()
    s_c = st.selectbox('Select a country',clist)
    labels = ['Women','']

    fig, ax = plt.subplots(figsize=(5, 5))
    ax = plt.pie(dama[dama['Country'] == s_c].squeeze().tolist()[1:3], labels=labels, wedgeprops={'edgecolor': 'black'},
            autopct='%1.1f%%',shadow=True,colors = ['#FFB6C1' , '#87CEFA'],explode=[0.1,0])
    st.pyplot(fig)
    st.text("All data is for the year 2018")
    st.write('A fun fact worth looking is that the country with greatest share of women in parliament is actually an '
             'African nation Rwanda.')
    st.write('In 2018, Papua New Guinea had zero seats held by women in the Parliament.')




