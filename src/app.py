

# your code here
import streamlit as st
import pickle
import pandas as pd

# model
with open('../models/LinearRegression_.sav', 'rb') as file:
    model = pickle.load(file)

# scaler
with open('../models/scalerOM.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

feature_names = scaler.get_feature_names_out()

st.markdown('<style>h1 { color: brown; }</style>', unsafe_allow_html=True)
# Website title
st.title("Insurance Calculator")

# mapping for region, sex and smoker


smoker_mapping = {
    'Yes': 0, 
    'No': 1
    }

sex_mapping = {
    'Female': 0, 
    'Male' : 1
    }

# user input
age = st.slider(
    'Plase, enter the age:',
    min_value=18,
    max_value=70,
    step = 1
    )



bmi = st.slider(
    'Body mass index (BMI):',
    min_value=15.0,
    max_value=53.0, 
    step = 0.1
    )

children = st.slider(
    'Number of children:', 
    min_value=0,
    max_value=7, 
    step = 1
    )

smoker_n = st.selectbox(
    'Are you a smoker?', 
    ['Yes', 'No'] 
    )



if st.button("Predict"):
    row = [
        age,
        
        smoker_mapping[smoker_n],
        children,
        bmi,
       
        ]

    scal_data = scaler.transform([row])
    y_pred = model.predict([row])

    st.write(f'The charge for your insurance is: ${y_pred[0]:,.2f}')