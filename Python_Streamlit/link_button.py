import streamlit as st

st.markdown("## Link Button")

image_list = ["google.jfif", "youTube.jfif"]
caption_list = ["Google link", "YouTube link"]
st.title("Link Button Example")
st.image(image_list, caption=caption_list, width=100)
st.subheader("Click the buttons below to visit the respective websites:")
st.link_button("Visit Google", "https://www.google.com")
st.link_button("Visit YouTube", "https://www.youtube.com")