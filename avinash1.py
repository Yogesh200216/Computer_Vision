import streamlit as st
import cv2
# Streamlit app title
st.title("First Name Display App")

# Input widget for first name
first_name = st.text_input("Enter your first name")

# Display the input first name
if first_name:
    st.write(f"Your first name is: {first_name}")
