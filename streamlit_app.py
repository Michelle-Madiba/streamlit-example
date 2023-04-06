import pandas as pd
import streamlit as st

st.title("My first Streamlit app")
st.write("Streamlit is fun")
st.write("welcome to my Streamlit app")
x=st.slider('Select value for x',0,10)
st.write('You selected X: ',x)
