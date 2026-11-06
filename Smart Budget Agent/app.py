import streamlit as st
import pandas as pd

st.title("💰 Smart Budget Agent")

income = st.number_input("Enter Monthly Income", min_value=0)

expense = st.number_input("Enter Monthly Expense", min_value=0)

if st.button("Calculate Budget"):

    savings = income - expense

    st.subheader("Budget Report")

    st.write("Income:", income)
    st.write("Expense:", expense)
    st.write("Savings:", savings)

    if savings > 0:
        st.success(f"You saved ₹{savings}")
    elif savings == 0:
        st.warning("No Savings")
    else:
        st.error("Expenses exceed income!")