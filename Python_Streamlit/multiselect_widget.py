import streamlit as st

st.markdown("## MultiSelect widget")

options = st.multiselect(
    "Select your favorite company:",['Youtube', 'Google', 'Whatsapp', 'Snapchat', 'Twitter'], default = None)

for x in options:
    if x == 'Youtube':
        st.image('youtube.jfif', width =100, caption = 'Youtube')
    elif x == 'Google':
        st.image('google.jfif', width =100, caption = 'Google')
    elif x == 'Whatsapp':
        st.image('whatsapp.jfif', width =100, caption = 'Whatsapp')
    elif x == 'Snapchat':
        st.image('snapchat.jfif', width =100, caption = 'Snapchat')
    elif x == 'Twitter':
        st.image('twitter.jfif', width =100, caption = 'Twitter')