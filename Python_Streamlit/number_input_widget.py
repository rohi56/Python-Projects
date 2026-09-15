import streamlit as st

st.markdown("## Number Input widget")

st.header("Calculator App")

number1 = st.number_input("Enter the first number:")
number2 = st.number_input("Enter the second number:")

buttons = st.columns(4)
with buttons[0]:
    add_button = st.button("Add")
    if add_button:
        result = number1 + number2
        st.write(f"The sum of {number1} and {number2} is: {result}")

with buttons[1]:
    subtract_button = st.button("Subtract")
    if subtract_button:
        result = number1 - number2
        st.write(f"The difference between {number1} and {number2} is: {result}")

with buttons[2]:
    multiply_button = st.button("Multiply")
    if multiply_button:
        result = number1 * number2
        st.write(f"The product of {number1} and {number2} is: {result}")

with buttons[3]:
    divide_button = st.button("Divide")
    if divide_button:
        if number2 != 0:
            result = number1 / number2
            st.write(f"The quotient of {number1} and {number2} is: {result}")
        else:
            st.write("Error: Division by zero is not allowed.")