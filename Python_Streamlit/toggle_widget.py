import streamlit as st

st.markdown("## Toggle widget")

st.header("Toggle Widget Example")

toggle = st.columns(2)

with toggle[0]:
    toggle_image = st.toggle("Enable Image")

with toggle[1]:
    toggle_video = st.toggle("Enable Video")

if toggle_image:
    st.image('img.jpg', caption='This is an image')

if toggle_video:
    st.video('video.mp4', format='video/mp4', start_time=0)