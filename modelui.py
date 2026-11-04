import streamlit as st
import joblib
import pandas as pd

pipeline = joblib.load(r"D:\Cbitss\model.joblib")

st.title = ("Student Performance Index")
st.write = ("Performance Predictor")

st.subheader = "Student Details"

Age = st.number_input("Age" , placeholder="Enter your age: ")

Study_Hours_Per_Day = st.number_input("Study_Hours_Per_Day", placeholder= "Enter Hours:")

Attendance_Percent = st.number_input("Attendance_Percent" , placeholder= "Enter Precentage")

Previous_Exam_Score = st.number_input("Previous_Exam_Score" , placeholder= "Enter previous_Exam_Score")

Assignment_Score = st.number_input("Assignment_Score" , placeholder= "Enter Assignment_Score")

Sleep_Hours = st.number_input("Sleep_Hours" , placeholder= "Enter Sleep_Hours")

Class_Participation_Percent = st.number_input("Class_Participation_Percent" , placeholder= "Enter Class_Participation_Percent")

Practice_Tests_Completed = st.number_input("Practice_Tests_Completed" , placeholder= "Enter Practice_Tests_Completed")

Extracurricular_Activity = st.selectbox("Extracurricular_Activity:" , ["Yes" , "no"])

Internet_Access = st.selectbox("Internet_Access:" , ["Yes" , "no"])

if st.button("Predict Performance_Class"):

    input_data = pd.DataFrame([[Age,Study_Hours_Per_Day,Attendance_Percent,Previous_Exam_Score, 
                                Assignment_Score,Sleep_Hours,Class_Participation_Percent,
                                Practice_Tests_Completed,Extracurricular_Activity,Internet_Access,]],

columns = ["Age",
"Study_Hours_Per_Day","Attendance_Percent","Previous_Exam_Score",
"Assignment_Score","Sleep_Hours","Class_Participation_Percent",
"Practice_Tests_Completed","Extracurricular_Activity", "Internet_Access"])

    prediction = pipeline.predict(input_data)

    st.success(f"Performance_class:{prediction[0]}")