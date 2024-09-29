import streamlit as st
import pandas as pd

st.title('Machine Learning app')

st.write('this app builds an ML model!')

with st.expander('Data'):

  st.write("**Raw Data**")
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X = df.drop('species', axis = 1)
  gX

  st.write('**Y**')
  Y = df.species
  Y

with st.expander('Data visualisation'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# data preperation
with st.sidebar:
  st.header('input features : ')

  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gender', ('Male', 'Female'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 42.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 14.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700, 6300, 4207 )
