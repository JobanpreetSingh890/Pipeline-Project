# import streamlit as st
# import joblib
# import pandas as pd
# pipeline = joblib.load(r"C:\Cbitss\model.joblib")

# st.title = ("Student Performance Index")
# st.write = ("Performance Predictor")

# st.subheader = "Student Details"

# Age = st.number_input("Age" , placeholder="Enter your age: ")

# Study_Hours_Per_Day = st.number_input("Study_Hours_Per_Day", placeholder= "Enter Hours:")

# Attendance_Percent = st.number_input("Attendance_Percent" , placeholder= "Enter Precentage")

# Previous_Exam_Score = st.number_input("Previous_Exam_Score" , placeholder= "Enter previous_Exam_Score")

# Assignment_Score = st.number_input("Assignment_Score" , placeholder= "Enter Assignment_Score")

# Sleep_Hours = st.number_input("Sleep_Hours" , placeholder= "Enter Sleep_Hours")

# Class_Participation_Percent = st.number_input("Class_Participation_Percent" , placeholder= "Enter Class_Participation_Percent")

# Practice_Tests_Completed = st.number_input("Practice_Tests_Completed" , placeholder= "Enter Practice_Tests_Completed")

# Extracurricular_Activity = st.selectbox("Extracurricular_Activity:" , ["Yes" , "no"])

# Internet_Access = st.selectbox("Internet_Access:" , ["Yes" , "no"])

# if st.button("Predict Performance_Class"):

#     input_data = pd.DataFrame([[Age,Study_Hours_Per_Day,Attendance_Percent,Previous_Exam_Score, 
#                                 Assignment_Score,Sleep_Hours,Class_Participation_Percent,
#                                 Practice_Tests_Completed,Extracurricular_Activity,Internet_Access,]],

# columns = ["Age",
# "Study_Hours_Per_Day","Attendance_Percent","Previous_Exam_Score",
# "Assignment_Score","Sleep_Hours","Class_Participation_Percent",
# "Practice_Tests_Completed","Extracurricular_Activity", "Internet_Access"])

#     prediction = pipeline.predict(input_data)

#     st.success(f"Performance_class:{prediction[0]}")


import streamlit as st
import joblib
import pandas as pd

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #101827, #192b46);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #aabbd4;
    font-size: 16px;
    margin-bottom: 35px;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #8dbdff;
    margin-bottom: 15px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 16px;
    padding: 20px;
}

.stNumberInput input {
    border-radius: 8px;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius: 8px;
}

.stButton button {
    width: 100%;
    height: 50px;
    border-radius: 10px;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    font-size: 17px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    border: 1px solid #ffffff;
    color: white;
}

.result-card {
    background: linear-gradient(120deg, #1d4ed8, #6d28d9);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
}

.result-label {
    color: #dbeafe;
    font-size: 17px;
}

.result-value {
    color: white;
    font-size: 32px;
    font-weight: bold;
    margin-top: 8px;
}

.footer {
    text-align: center;
    color: #8293ad;
    margin-top: 40px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    return joblib.load(r"C:\Cbitss\model.joblib")

pipeline = load_model()


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🎓 Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Smart Machine Learning Based Student Performance Analysis</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- STUDENT INPUT FORM ----------------

with st.form("student_form"):

    st.markdown(
        '<div class="section-title">👨‍🎓 Student Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        Age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            value=20
        )

        Study_Hours_Per_Day = st.number_input(
            "Study Hours Per Day",
            min_value=0.0,
            max_value=24.0,
            value=5.0,
            step=0.5
        )

        Attendance_Percent = st.number_input(
            "Attendance Percentage",
            min_value=0.0,
            max_value=100.0,
            value=85.0
        )

        Previous_Exam_Score = st.number_input(
            "Previous Exam Score",
            min_value=0.0,
            max_value=100.0,
            value=75.0
        )

        Assignment_Score = st.number_input(
            "Assignment Score",
            min_value=0.0,
            max_value=100.0,
            value=80.0
        )

    with col2:

        Sleep_Hours = st.number_input(
            "Sleep Hours",
            min_value=0.0,
            max_value=24.0,
            value=8.0,
            step=0.5
        )

        Class_Participation_Percent = st.number_input(
            "Class Participation Percentage",
            min_value=0.0,
            max_value=100.0,
            value=80.0
        )

        Practice_Tests_Completed = st.number_input(
            "Practice Tests Completed",
            min_value=0,
            max_value=1000,
            value=5
        )

        Extracurricular_Activity = st.selectbox(
            "Extracurricular Activity",
            ["Yes", "No"]
        )

        Internet_Access = st.selectbox(
            "Internet Access",
            ["Yes", "No"]
        )

    st.divider()

    predict_button = st.form_submit_button(
        "🚀 Predict Student Performance"
    )


# ---------------- PREDICTION ----------------

if predict_button:

    input_data = pd.DataFrame([{
        "Age": Age,
        "Study_Hours_Per_Day": Study_Hours_Per_Day,
        "Attendance_Percent": Attendance_Percent,
        "Previous_Exam_Score": Previous_Exam_Score,
        "Assignment_Score": Assignment_Score,
        "Sleep_Hours": Sleep_Hours,
        "Class_Participation_Percent": Class_Participation_Percent,
        "Practice_Tests_Completed": Practice_Tests_Completed,
        "Extracurricular_Activity": Extracurricular_Activity,
        "Internet_Access": Internet_Access
    }])

    try:

        prediction = pipeline.predict(input_data)

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">
                    Student Performance Prediction
                </div>
                <div class="result-value">
                    {prediction[0]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("Prediction generated successfully!")

    except Exception as e:

        st.error(f"Prediction Error: {e}")


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    Student Performance Predictor | Powered by Machine Learning
</div>
""", unsafe_allow_html=True)
