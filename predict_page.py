import streamlit as st
import pickle 
import numpy as np
import pandas as pd

st.set_page_config(page_title = 'Heart Disease Prediction', page_icon = '❤️')

model = pickle.load(open('finalized_model.pkl', 'rb'))

def gender_encoder(var):
    if var == "Male":
        r_value = 1
    else:
        r_value = 0
    return r_value


def yn_encoder(var):
    if var == "Yes":
        r_value = 1
    else:
        r_value = 0
    return r_value

def show_page():
    st.title("Heart Disease Prediction")
    st.write("""### We need some information""")

    yes_no = ("Yes", "No")
    is_sex = ("Male", "Female")

    gender = gender_encoder(st.selectbox("Gender", is_sex))
    height = st.slider("What is your height (cm)", 0, 200, 0)
    weight = st.slider("What is your height (kg)", 0, 200, 0)
    age = st.slider("What is your age", 0, 100, 0)
    smoking = yn_encoder(st.selectbox("Do you smoke", yes_no))
    alochol = yn_encoder(st.selectbox("Do you consume alcohol", yes_no))
    p_health = st.slider("Rate your phyiscal health", 0, 100, 0)
    stroke = yn_encoder(st.selectbox("Have you ever had a stroke", yes_no))
    walking = yn_encoder(st.selectbox("Do you have difficulty walking", yes_no))
    kidney = yn_encoder(st.selectbox("Do you have kidney disease", yes_no))
    m_health = st.slider("Rate your mental health", 0, 100, 0)
    asthma = yn_encoder(st.selectbox("Do you have asthma", yes_no))
    sleep = st.slider("How many hours of sleep do you get", 0, 12, 8)
    active = yn_encoder(st.selectbox("Are you physically active", yes_no))
    cancer = yn_encoder(st.selectbox("Do you have skin cancer", yes_no))
    diabetic = yn_encoder(st.selectbox("Are you diabetic", yes_no))

    bmi = weight/ ((height/100)**2)

    ok = st.button("Predict risk of Cardiovascular Disease")
    if ok:
        data = {'BMI': [bmi], 'Smoking': [smoking],
            'AlcoholDrinking': [alochol], 'Stroke': [stroke], 'PhysicalHealth': [p_health], 
            'MentalHealth': [m_health], 'DiffWalking': [walking], 'Sex': [gender], 'AgeCategory': [age], 'Diabetic': [diabetic],
            'PhysicalActivity': [active], 'SleepTime': [sleep], 'Asthma': [asthma], 
            'KidneyDisease': [kidney], 'SkinCancer': [cancer]}

        df = pd.DataFrame(data)

        risk = model.predict(df)
        st.subheader(f"You have a {risk[0]:.4f}% chance of having Cardiovascular Disease")