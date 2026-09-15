import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("JavaScript")
    st.image("javascript.png")
    st.link_button("JavaScript", "https://www.javascript.com/")
with col2:
    st.header("Python")
    st.image("python.png")
    st.link_button("Python", "https://www.python.org/")
with col3:
    st.header("Java")
    st.image("java.png")
    st.link_button("Java", "https://www.java.com/")