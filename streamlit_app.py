import pandas as pd
import streamlit as st
import plotly.express as  px

st.set_page_config(page_title="Flights Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("My first Streamlit app")
st.write("Streamlit is fun")
st.write("welcome to my Streamlit app")
x=st.slider('Select value for x',0,10)
st.write('You selected X: ',x)
