import streamlit as st

st.title("🛒 Shopping Cart Value Calculator")

# Shirt details
shirt_price = st.number_input("Enter the price of a Shirt (₹)", min_value=0.0, format="%.2f")
shirt_quantity = st.number_input("Enter the quantity of Shirts", min_value=0, step=1)

# Pants details
pants_price = st.number_input("Enter the price of Pants (₹)", min_value=0.0, format="%.2f")
pants_quantity = st.number_input("Enter the quantity of Pants", min_value=0, step=1)

# Oil details
oil_price = st.number_input("Enter the price of Oil (1 Liter) (₹)", min_value=0.0, format="%.2f")
oil_quantity = st.number_input("Enter the quantity of Oil (Liters)", min_value=0, step=1)

# Calculate button
if st.button("Calculate Total"):
    total_cost = (
        (shirt_price * shirt_quantity)
        + (pants_price * pants_quantity)
        + (oil_price * oil_quantity)
    )

    st.success(f"🛍️ Total Cost: ₹{total_cost:.2f}")