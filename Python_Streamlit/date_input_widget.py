import streamlit as st

st.markdown("## Date Input widget")

st.header("Number of days between two dates")

name1 = st.text_input("Enter your name:", key="date_calculator_name")
start_date = st.date_input("Select the start date:")
end_date = st.date_input("Select the end date:")

button = st.button("Calculate Days")
if button:
    if start_date and end_date:
        days_difference = (end_date - start_date).days
        st.write(f"Hello, {name1}! The number of days between {start_date} and {end_date} is: {days_difference} days.")
    else:
        st.write("Please select both start and end dates.")




