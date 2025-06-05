import streamlit as st
import joblib
import numpy as np
model=joblib.load("diabetes_model.pkl")
st.title("Diabetes Prediction App")
st.write("Enter the following information to predict diabetes status.")
pragnancies=st.number_input("Number of Pragnancies",0,20,1)
glocuse=st.number_input("Glocuse Level",0,200,100)
blood_pressure=st.number_input("Blood Pressure",0,150,70)
skin_thickness=st.number_input("Skin Thickness",0,100,20)
insulin=st.number_input("Insulin Level",0.0,900.0,80.0)
bmi=st.number_input("BMI",0.0,70.0,25.0)
dpf=st.number_input("Diabetes Pedigree Function",0.0,2.5,0.5)
age=st.number_input("Age",10,100,30)
if st.button("Predict"):
    user_data=np.array([[pragnancies,glocuse,blood_pressure,skin_thickness,insulin,bmi,dpf,age]])
    prediction=model.predict(user_data)
    if prediction[0]==1:
        st.error("The person is likely to have diabetes")
    else:
        st.success("The person is not likely to have diabetes")