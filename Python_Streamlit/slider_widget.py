import streamlit as st

st.markdown("## Slider widget")

size = st.slider("Select a image size:", 200, 800, 200)
st.image('img.jpg', width=size)


