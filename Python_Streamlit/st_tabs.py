import streamlit as st

tab1, tab2, tab3 = st.tabs(["Football", "Basketball", "Tennis"])

with tab1:
    st.header("Football")
    st.image("football.jpg")
    st.write("Football is a team sport played between two teams of eleven players with a spherical ball.")

with tab2:
    st.header("Basketball")
    st.image("basketball.jpg")
    st.write("Basketball is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court.")

with tab3:
    st.header("Tennis")
    st.image("tennis.jpg")
    st.write("Tennis is a racket sport that can be played individually against a single opponent or between two teams of two players each.")