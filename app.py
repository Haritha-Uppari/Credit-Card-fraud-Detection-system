import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("fraud_model.pkl","rb"))

st.title("Credit Card Fraud Detection System")

st.subheader("Enter Card Details")

card_number = st.text_input("Card Number")
card_holder = st.text_input("Card Holder Name")
expiry = st.text_input("Expiry Date")
cvv = st.text_input("CVV")

amount = st.number_input("Transaction Amount")
time = st.number_input("Transaction Time")

if st.button("Check Transaction"):

    # dataset requires 30 features
    features = [0]*28

    input_data = [time] + features + [amount]

    prediction = model.predict([input_data])

    if prediction[0] == 1:
        st.error("Fraud Transaction Detected")
    else:
        st.success("Transaction is Safe")