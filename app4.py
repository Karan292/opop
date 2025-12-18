import streamlit as st
st.title("simple calculator app")
num1 = st.number_input("enter first number:")
num2 = st.number_input("enter second number:")

operation = st.selectbox("select operation", ["add" , "subtract", "multiply", "divide"])

if st.button("calculator"):
    if operation == "add":
        st.write(num1 + num2)
    elif operation == "subtract":
        st.write(num1 - num2)
    elif operation == "multiply":
        st.write(num1 * num2)
    elif operation == "divide":
        if num2 != 0:
            st.write(num1 / num2)
        else:
            st.write("Error: Division by zero is not allowed.")