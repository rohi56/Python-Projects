import streamlit as st

st.markdown("## Checkbox widget")

image_list = ["google.jfif", "youTube.jfif"]
caption_list = ["Google link", "YouTube link"]

checks = st.columns(2)
with checks[0]:
    images = st.checkbox("Do you want to see the images?")
with checks[1]:
     codes = st.checkbox("Do you want to see the code?")

if images:
    st.write("Here are the images:")
    st.image(image_list, caption=caption_list, width=100)

if codes:
    st.code("print('Hello, World!')", language="python ")