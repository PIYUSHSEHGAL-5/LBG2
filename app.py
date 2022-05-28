import streamlit as st
from multiapp import MultiApp
from apps import AbouttheProject, HDI, model,GE,Env, Environ # import your app modules here

app = MultiApp()



st.title('Looking Beyond GDP ...')
st.text(' ')
st.text('Development is about transforming the Lives of People, not just transforming ')
st.text('Economies.                                                  -Joseph E. Stiglitz')
# Add all your application here

app.add_app("About the Project", AbouttheProject.app)
app.add_app("Overall Human Development ", HDI.app)
app.add_app("A Global View", Env.app)
app.add_app("Population", model.app)
app.add_app("Gender Equality", GE.app)
app.add_app("Environment", Environ.app)
st.text('  ')
st.text(' ')
st.text(' ')
# The main app
app.run()
