import streamlit as st

st.title("💰 Simple Interest Calculator")

# User inputs
principal = st.number_input("Enter the Principal (₹)", min_value=0.0, format="%.2f")
rate = st.number_input("Enter the Rate of Interest (%)", min_value=0.0, format="%.2f")
years = st.number_input("Enter the Number of Years", min_value=0, step=1)
months = st.number_input("Enter the Number of Months", min_value=0, max_value=11, step=1)

# Calculate button
if st.button("Calculate"):
    time = years + (months / 12)
    interest = (principal * rate * time) / 100
    total_amount = principal + interest

    st.success(f"Interest: ₹{interest:.2f}")
    st.success(f"Total Amount: ₹{total_amount:.2f}")