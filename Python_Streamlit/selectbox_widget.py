import streamlit as st

st.markdown("## Selectbox widget")
car_info = {
    "Toyota": "Toyota is a Japanese automotive manufacturer known for its reliable and fuel-efficient vehicles",
    "Honda": "Honda is a Japanese automotive manufacturer known for its reliability and innovation",
    "Ford": "Ford is an American automotive manufacturer known for its trucks and SUVs",
    "Chevrolet": "Chevrolet is an American automotive manufacturer known for its muscle cars and trucks",
    "Nissan": "Nissan is a Japanese automotive manufacturer known for its affordable and fuel-efficient vehicles",
    "BMW": "BMW is a German automotive manufacturer known for its luxury cars and motorcycles",
    "Mercedes-Benz": "Mercedes-Benz is a German automotive manufacturer known for its luxury cars and commercial vehicles",
    "Audi": "Audi is a German automotive manufacturer known for its luxury cars and quattro all-wheel-drive technology",
    "Volkswagen": "Volkswagen is a German automotive manufacturer known for its affordable and reliable vehicles",
    "Hyundai": "Hyundai is a South Korean automotive manufacturer known for its affordable and fuel-efficient vehicles"
}
st.header("Select a Car Brand")

option = st.selectbox(
    "Which car brand do you prefer?", 
    ("Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Mercedes-Benz", "Audi", "Volkswagen", "Hyundai"), index = None)

if option:
    st.write(f"You selected: {option}")
    st.write(f"Information about {option}: {car_info[option]}")