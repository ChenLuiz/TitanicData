import pandas as pd
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Streamlit page configurations
st.set_page_config(page_title = "Titanic Data", layout="wide", initial_sidebar_state="collapsed")

# Setting amount of columns in streamlit
col1, col2, col3 = st.columns(3)

with col1:
  # Chart 1 Histogram of Age
  Hist_Age = alt.Chart(data).mark_bar().encode(
      alt.X("Age:Q", bin = True),
      y = 'count()'
  )
  # Importing altair Chart to Streamlit
  st.altair_chart(Hist_Age)

with col2:
  # Chart 2 scatter plot of Age and Fare
  Scatter = alt.Chart(data).mark_circle().encode(
      x = 'Fare',
      y = 'Age',
      color = 'Survived',
      tootip = ['Age', 'Fare', 'Survived', 'Name']
  ).interactive()
  st.altair_chart(Scatter)

with col3:
  # Chart 3 Histogram of Fare
  Hist_Fare = alt.Chart(data).mark_bar().encode(
      alt.X("Fare:Q", bin = True),
      y = 'count()'
  )
  st.altair_chart(Hist_Fare)
