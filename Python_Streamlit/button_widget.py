import streamlit as st

st.markdown("## Buttons and Widgets")
car_name = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Mercedes-Benz", "Audi", "Volkswagen", "Hyundai"]
car = st.text_input("Enter your favorite car:")


button = st.button("Check Availability!")
if button == True   :
    have_it = car.lower() in [c.lower() for c in car_name]
    if have_it:
        st.success(f"Yes, we have {car} in stock!")
    else:
        st.error(f"Sorry, we don't have {car} in stock.")