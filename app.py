import streamlit as st
from textblob import TextBlob
import plotly.graph_objects as go
import altair as alt
import numpy as np


st.markdown("# Linkedin User Prediction App!")
st.markdown("## Please answer the following questions")

st.markdown("### 1. How old are you?")
streamlit.slider("Choose your age:", min_value=18,max_value=99,step=1)

st.markdown("### 2. What's the highest level of school/degree you completed?")
options=("1. Less than high school",
         "2. High school incomplete",
         "3. High school graduate",
         "4. Some college, no degree",
         "5. Two-year associate degree from a college or university",
         "6. Four-year college or university degree(Bachelor's)",
         "7. Some postgraduate or professional schooling, no postgraduate degree",
         "8. Postgraduate or professional degree, including master's, doctoral, medical or law degree")

st.markdown("### 3. What's your current annual income?")
options=("1. less than $10,000",
         "2. 10 to under $20,000",
         "3. 20 to under $30,000",
         "4. 30 to under $40,000",
         "5. 40 to under $50,000",
         "6. 50 to under $75,000",
         "7. 75 to under $100,000",
         "8. 100 to under $150,000",
         "9. More than $150,000",
         "10. Don't know/Refuse to answer")



status = st.radio("Select Birth Gender:", ('Male','Female'))
if (status == 'Male'):
    "gender" == 1
else:
    "gender" == 0

st.markdown("### 5. What's your current marital status? ")
st.selectbox("Married", "Not Married")

st.markdown("### 6. Are you a parent of a child under living in your home?"):
st.selectbox("Yes","No")