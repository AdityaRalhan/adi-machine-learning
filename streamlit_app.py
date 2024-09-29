import streamlit as st
import pandas as pd

st.title('Machine Learning app')

st.write('this app builds an ML model!')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df
