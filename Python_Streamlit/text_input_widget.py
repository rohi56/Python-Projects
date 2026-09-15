import streamlit as st

st.markdown("## Text Input widget")

name = st.text_input("Enter your name:")
last_name = st.text_input("Enter your last name:")

button = st.button("show name")
if button == True:
    st.write(f"Hello, {name} {last_name}!")