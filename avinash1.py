import streamlit as st
import cv2

# Set an environment variable for OpenCV to run in headless mode
import os
os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "0"

# Streamlit app title
st.title("First Name Display App")

# Input widget for first name
first_name = st.text_input("Enter your first name")

# Display the input first name
if first_name:
    st.write(f"Your first name is: {first_name}")
