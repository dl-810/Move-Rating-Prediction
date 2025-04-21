import streamlit as st

st.title("My First App")

name = st.test_input("What's your name?")
if name:
  st.write(f"Hello, {name}!")
