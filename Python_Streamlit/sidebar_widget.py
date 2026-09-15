import streamlit as st

st.header("Best Performance of the Show")
st.video("https://www.youtube.com/watch?v=GqaGrD8qquQ&list=RDGqaGrD8qquQ&start_radio=1")

with st.sidebar:
    add_selectbox = st.selectbox(
        "How was the performance:",
        ["Excellent", "Best", "Good"]
    )

    add_input = st.text_input("Enter your comments:", "Type Here ...")
    add_radio = st.radio("Do you want to see the complete show:", ("Yes", "No"))
    sdd_submit_button = st.button("Submit")

if sdd_submit_button:
    st.write("Thank you for your feedback!")
