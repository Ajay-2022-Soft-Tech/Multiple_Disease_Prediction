# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:21:38 2024

@author: dewan
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open("model/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("model/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("model/parkinsons_model.sav", 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
                           default_index=0,
                           icons=['activity', 'heart-pulse-fill', 'person'])

# Main content
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input fields
    st.subheader('Enter Patient Details')
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
        glucose = st.number_input('Glucose Level', min_value=0)
        blood_pressure = st.number_input('Blood Pressure', min_value=0)
    with col2:
        skin_thickness = st.number_input('Skin Thickness', min_value=0)
        insulin = st.number_input('Insulin Level', min_value=0)
        bmi = st.number_input('BMI', min_value=0.0)
    with col3:
        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0)
        age = st.number_input('Age', min_value=0)

    # Prediction button
    if st.button('Predict Diabetes'):
        prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness,
                                              insulin, bmi, diabetes_pedigree_function, age]])
        result = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
        st.success(result)

elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields
    st.subheader('Enter Patient Details')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=0)
        sex = st.selectbox('Sex', ['Male', 'Female'])
        cp = st.selectbox('Chest Pain Types', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    with col2:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0)
        chol = st.number_input('Serum Cholesterol', min_value=0)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['False', 'True'])
    with col3:
        restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0)
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])

    # Prediction button
    if st.button('Predict Heart Disease'):
        prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang]])
        result = 'The person is having heart disease' if prediction[0] == 1 else 'The person does not have any heart disease'
        st.success(result)

elif selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields
    st.subheader('Enter Patient Details')
    col1, col2, col3 = st.columns(3)
    with col1:
        fo = st.number_input('MDVP:Fo (Hz)', min_value=0.0)
        fhi = st.number_input('MDVP:Fhi (Hz)', min_value=0.0)
        flo = st.number_input('MDVP:Flo (Hz)', min_value=0.0)
        jitter_percent = st.number_input('MDVP:Jitter (%)', min_value=0.0)
        jitter_abs = st.number_input('MDVP:Jitter (Abs)', min_value=0.0)
    with col2:
        rap = st.number_input('MDVP:RAP', min_value=0.0)
        ppq = st.number_input('MDVP:PPQ', min_value=0.0)
        ddp = st.number_input('Jitter:DDP', min_value=0.0)
        shimmer = st.number_input('MDVP:Shimmer', min_value=0.0)
        shimmer_db = st.number_input('MDVP:Shimmer (dB)', min_value=0.0)
    with col3:
        apq3 = st.number_input('Shimmer:APQ3', min_value=0.0)
        apq5 = st.number_input('Shimmer:APQ5', min_value=0.0)
        apq = st.number_input('MDVP:APQ', min_value=0.0)
        dda = st.number_input('Shimmer:DDA', min_value=0.0)
        nhr = st.number_input('NHR', min_value=0.0)
    with col1:
        hnr = st.number_input('HNR', min_value=0.0)
        rpde = st.number_input('RPDE', min_value=0.0)
        dfa = st.number_input('DFA', min_value=0.0)
        spread1 = st.number_input('Spread1', min_value=0.0)
        spread2 = st.number_input('Spread2', min_value=0.0)
    with col2:
        d2 = st.number_input('D2', min_value=0.0)
        ppe = st.number_input('PPE', min_value=0.0)

    # Prediction button
    if st.button("Predict Parkinson's Disease"):
        prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db,
                                                apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])
        result = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(result)
