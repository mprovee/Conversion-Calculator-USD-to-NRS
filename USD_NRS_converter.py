import streamlit as st

st.title("USD to NRS Converter")

amount = st.text_input("What amount do you want to convert (in USD)?")

if amount:
    try:
        total_conversion = float(amount) * 144
        st.write("The total amount in NRS is:", total_conversion)
    except ValueError:
        st.error("Please enter a valid number.")
