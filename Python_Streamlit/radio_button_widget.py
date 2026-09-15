import streamlit as st

st.markdown("## Radio Button widget")

st.header("Radio Button Example")

radio_button = st.radio("Choose an option:", ("Option 1", "Option 2", "Option 3"), index = None)
if radio_button == "Option 1":
    st.write("You selected Option 1")
elif radio_button == "Option 2":
    st.write("You selected Option 2")
elif radio_button == "Option 3":
    st.write("You selected Option 3")