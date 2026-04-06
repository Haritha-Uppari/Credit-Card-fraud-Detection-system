import streamlit as st

st.title("Credit Card Fraud Detection System")

st.subheader("Enter Card Details")

# Input fields
card_number = st.text_input("Card Number")
card_holder = st.text_input("Card Holder Name")
expiry = st.text_input("Expiry Date (MM/YY)")
cvv = st.text_input("CVV")

amount = st.number_input("Transaction Amount", min_value=0.0)
time = st.number_input("Transaction Time", min_value=0.0)

# Button
if st.button("Check Transaction"):

    # Simple fraud detection rule
    if amount > 2000:
        st.error("Fraud Transaction Detected 🚨")
    else:
        st.success("Transaction is Safe ✅")