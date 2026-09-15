import streamlit as st

st.markdown("## Text Area widget")

txt = st.text_area("Text to Analyze", placeholder= "Type Here... ", max_chars= 200, height= 100)

analyze_button = st.button("Analyze Text")
if analyze_button:
    if txt:
        word_count = len(txt.split())
        char_count = len(txt)
        st.write(f"Word Count: {word_count}")
        st.write(f"Character Count: {char_count}")
    else:
        st.write("Please enter some text to analyze.")