import streamlit as st
st .title("interactive streamlit app")
name =st.text_input("enter your name: ")
st.write(f"hello,{name}!welcome to streamlit.")
