import streamlit as st
import time

time_input = st.text_input("Enter a time:")
button = st.button("Start")

if button:
    with st.empty():
        for seconds in range(int(time_input)):
            st.write(f"Time elapsed: {seconds} seconds")
            time.sleep(1)
        st.image("finish.png")
    