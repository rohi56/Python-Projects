import streamlit as st

st.markdown("## Download Button")

st.image('img.jpg', caption='This is an image')  
file_name = st.text_input("Enter the file name to download:")

with open('img.jpg', 'rb') as f:
    btn = st.download_button(
        label="Download Image",
        data=f,
        file_name=file_name,
        mime="image/jpeg"
    )
