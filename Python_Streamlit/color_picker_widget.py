import streamlit as st

st.header("Color Picker Widget")

color = st.color_picker("Pick a color:", "#00f900")
st.write(f"You selected the color: {color}")
st.markdown(f"<span style='color:{color}'>This text is in the selected color!</span>", unsafe_allow_html=True)