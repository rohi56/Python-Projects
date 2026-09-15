import streamlit as st

first_team = st.text_input("Enter the name of the first team:", key="first_team_name")

second_team = st.text_input("Enter the name of the second team:", key="second_team_name")

time_input = st.time_input("Select the match time:")

button = st.button("set match alarm ")

if button:
    if first_team and second_team and time_input:
        st.write(f"Alarm set for the match between {first_team} and {second_team} at {time_input}.")
    else:
        st.write("Please enter both team names and select a match time.")
