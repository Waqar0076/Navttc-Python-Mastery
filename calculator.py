# python -m venv .venv
# .venv\Script\activate
# pip install streamlit
# streamlit run calculator.py

import streamlit as st

st.title("Simple Calculator")

# context-manager 
with st.form(key="calculator_form"):
    st.header("Enter Two Numbers")

    num1 = st.number_input("First number:",step=1)
    num2 = st.number_input("Second number:",step=1)

    operation = st.selectbox(
        "Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"]
    )
    
    submit = st.form_submit_button("Calculate")

# Process calculation after submission
if submit:
    if operation == "Add":
        result = num1 + num2
        st.success(f"{num1} + {num2} = {result}")

    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"{num1} - {num2} = {result}")

    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"{num1} × {num2} = {result}")

    elif operation == "Divide":
        if num2 == 0:
            exp = ZeroDivisionError("Trying to divide by Zero")
            st.exception(exp)
            st.error("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            st.success(f"{num1} ÷ {num2} = {result}")