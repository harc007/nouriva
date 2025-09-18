import streamlit as st

st.title("My Simple Streamlit App")
st.write("Hello, Streamlit Community Cloud!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Welcome, {name}!")
