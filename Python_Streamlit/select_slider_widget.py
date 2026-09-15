import streamlit as st

st.markdown("## Select Slider widget")

st.header("Consumer Loan Interest Rate Calculator")

loan_amount = st.select_slider(
    "Select the loan amount:",
    options=list(range(1000, 100001, 1000)), 
    value=50000
)

loan_term = st.select_slider(
    "Select the loan term (in years):",
    options=list(range(1, 31)),
    value=5
)

st.subheader("Interest Rate Calculation")
calculated_interest_rate = (loan_amount * 0.05 * loan_term) / 100
st.write(f"Loan Amount: ${loan_amount}")
st.write(f"Loan Term: {loan_term} years")
st.write(f"Calculated Interest Rate: ${calculated_interest_rate:.2f}")