import streamlit as st
import pickle
import numpy as np

st.title("AI Student Performance & Career Recommendation")

model = pickle.load(open("../models/model.pkl", "rb"))

attendance = st.slider("Attendance (%)", 50, 100, 75)
study_hours = st.slider("Study Hours per Day", 1, 10, 3)
gender = st.selectbox("Gender", ["Male", "Female"])
gender = 0 if gender == "Male" else 1

if st.button("Predict"):
    data = np.array([[attendance, study_hours, gender]])
    result = model.predict(data)[0]
    st.success(f"Predicted Score: {result:.2f}")

    if result > 85:
        st.write("Career Suggestion: AI Engineer / Data Scientist")
    elif result > 65:
        st.write("Career Suggestion: Data Analyst")
    else:
        st.write("Improve basics & consistency")
