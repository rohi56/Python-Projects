import streamlit as st

with st.expander("JavaScript"):
    with st.container(border=True):
        st.header("JavaScript")
        st.image("javascript.png", width=200)
        st.link_button("JavaScript", "https://www.javascript.com/")

with st.expander("Python"):
    with st.container(border=True):
        st.header("Python")
        st.image("python.png", width=200)
        st.link_button("Python", "https://www.python.org/")

with st.expander("Java"):
    with st.container(border=True):
        st.header("Java")
        st.image("java.png", width=200)
        st.link_button("Java", "https://www.java.com/")
