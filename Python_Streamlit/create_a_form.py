import streamlit as st
from datetime import date

with st.form(key="my_form"):
    name = st.text_input("Enter your name:")
    last_name = st.text_input("Enter your last name:")
    age = st.slider("Enter your age:", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
    date_of_birth = st.date_input(
        "Select your date of birth:",
        min_value=date(1975, 1, 1),
        max_value=date.today(),
    )
    submit = st.form_submit_button("Submit")
if submit:
    st.success("Form submitted successfully!")
    st.write(f"Name: {name}")
    st.write(f"Last Name: {last_name}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Date of Birth: {date_of_birth}")