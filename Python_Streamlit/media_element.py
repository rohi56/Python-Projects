import streamlit as st

st.markdown("---")
st.markdown("## Media Elements")

st.image('img.jpg', caption='This is an image')  
st.video('video.mp4', format='video/mp4', start_time=0)