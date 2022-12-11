import streamlit as st
from textblob import TextBlob
import plotly.graph_objects as go
import altair as alt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#prediction model 
s = pd.read_csv("./social_media_usage1.csv")

def clean_sm(x):
    x = np.where(x == 1, 1, 0)
    return x

ss = pd.DataFrame()
ss["sm_li"] = clean_sm(s["web1h"])
ss["income"] = s["income"]
ss.loc[ss["income"] > 9, "income"] = "missing"
ss["educ2"] = s["educ2"]
ss.loc[ss["educ2"] > 8, "educ2"] = "missing"
ss["par"] = clean_sm(s["par"])
ss["marital"] = clean_sm(s["marital"])
ss["gender"] = clean_sm(s["gender"])
ss["age"] = s["age"]
ss.loc[ss["age"] > 98, "age"] = "missing"
ss.replace("missing", np.nan, inplace=True)
ss = ss.dropna()
ss["age"] = ss["age"].astype(int)
ss["income"] = ss["income"].astype(int)
ss["educ2"] = ss["educ2"].astype(int)


y = ss["sm_li"]
x = ss[["age","educ2","income","gender","par","marital"]]

x_train,x_test,y_train,y_test = train_test_split(x,
                                                y,
                                                stratify = y,
                                                test_size = 0.2,
                                                random_state=987
                                                )

lr = LogisticRegression(class_weight="balanced")
lr.fit(x_train,y_train)

st.markdown("# Welcome to the Linkedin User Prediction App")
st.markdown("#### (Designer: Anita Zeng)")
st.markdown("### Please answer the following questions:")

#selection setup
age = st.slider("Choose your age:", min_value=18,max_value=99,step=1)

educ2 = st.selectbox(label ="What's the highest level of school/degree you completed?",
options=("Less than high school",
         "High school incomplete",
         "High school graduate",
         "Some college, no degree",
         "Two-year associate degree from a college or university",
         "Four-year college or university degree(Bachelor's)",
         "Some postgraduate or professional schooling, no postgraduate degree",
         "Postgraduate or professional degree, including master's, doctoral, medical or law degree"))
income = st.selectbox(label = " What's your current annual income?",
options=("less than $10,000",
         "10 to under $20,000",
         "20 to under $30,000",
         "30 to under $40,000",
         "40 to under $50,000",
         "50 to under $75,000",
         "75 to under $100,000",
         "100 to under $150,000",
         "More than $150,000",
         "Don't know/Refuse to answer"))
gender = st.selectbox(label = "Select birth gender",
options=("Female","Male"))

marital = st.selectbox(label = "What's your current marital status?",
options=("Married", "Not Married"))

par = st.selectbox(label = "Are you a parent of a child under 18 living in your home? ",
options=("Yes", "No"))

#define the prediction function
def prediction(age,educ2,income,gender,par,marital):
    if educ2 == "Less than high school":
        educ2 = 1
    elif educ2 ==  "High school incomplete":
        educ2 = 2
    elif educ2 == "High school graduate":
        educ2 = 3
    elif educ2 == "Some college, no degree":
        educ2 = 4
    elif educ2 == "Two-year associate degree from a college or university":
        educ2 = 5
    elif educ2 == "Four-year college or university degree(Bachelor's)":
        educ2 = 6
    elif educ2 == "Some postgraduate or professional schooling, no postgraduate degree":
        educ2 = 7
    else:
        educ2 = 8



    if income == "less than $10,000":
        income = 1
    elif income == "10 to under $20,000":
        income = 2
    elif income == "20 to under $30,000":
        income = 3
    elif income == "30 to under $40,000":
        income = 4
    elif income == "40 to under $50,000":
        income = 5
    elif income == "50 to under $75,000":
        income = 6
    elif income == "75 to under $100,000":
        income = 7
    elif income == "100 to under $150,000":
        income = 8
    elif income == "More than $150,000":
        income = 9
    else:
        income = "Missing"




    if gender == "Female":
        gender = 0
    else:
        gender = 1


    if marital == "Married":
        marital = 1
    else:
        marital = 0

    if par == "Yes":
        par = 1
    else:
        par = 0

    prediction = lr.predict([[age,educ2,income,gender,marital,par]])
    probability = lr.predict_proba([[age,educ2,income,gender,marital,par]])

    if prediction == 0:
        pred = (f"You are NOT a Linkedin User; Your Linkedin user probability: {[probability[0][1]]}")
    else:
        pred = (f"You are a Linkedin User; Your Linkedin user probability:{[probability[0][1]]}")

    return pred



if st.button("Predict"):
    result = prediction(age,educ2,income,gender,marital,par)
    st.markdown(result)
    
    
  




    