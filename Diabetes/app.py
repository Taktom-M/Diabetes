import streamlit as st
import pandas as pd
import joblib

model = joblib.load('Diabetes.pkl')
st.title('Healthcare Diabetes Prediction App')

st.divider()

st.markdown('You can get Healthcare of Diabetes after entering the values & pressing to the predict button')

st.divider()

Pregnancies = st.number_input('Pregnancies', min_value=0, value=0)
Glucose = st.number_input('Glucose', min_value=0, value=0)
BloodPressure = st.number_input('Blood Pressure', min_value=0, value=50)
SkinThickness = st.number_input('Skin Thickness', min_value=0, value=0)
Insulin = st.number_input('Insulin', min_value=0, value=400)
BMI = st.number_input('BMI', min_value=0, value=40)
DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0, value=0)
Age = st.number_input('Age', min_value=20, value=40)

# Define preduction button
if st.button('Predict') :
    input_data = pd.DataFrame([{
        'Pregnancies' : Pregnancies,
        'Glucose' : Glucose,
        'BloodPressure' : BloodPressure,
        'SkinThickness' : SkinThickness	,
        'Insulin' : Insulin,
        'BMI' : BMI,
        'DiabetesPedigreeFunction' : DiabetesPedigreeFunction,
        'Age' : Age
    }])
    prediction = model.predict(input_data)[0]
    
    st.subheader(f"Prediction : '{int(prediction)}'")
    
    if prediction == 1 :
        st.error("The person have diabetic")
        
    else :
        
        st.success("The person not have diabetic")