import streamlit as st

st.title("hello")
import streamlit as st

st.title("My First App")
st.write("Hello World 👋")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello {name} 😊")


import streamlit as st

st.title("Chatbot")

user_input = st.text_input("You:")

if user_input:
    st.write("Bot:", user_input[::-1])  # reverse text as demo    