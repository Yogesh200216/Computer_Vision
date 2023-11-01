import cv2
import numpy as np
import streamlit as st

# Define the Streamlit app
st.title('Image Enhancement')

# Upload an image using Streamlit's file uploader
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)

    # Check if the image was loaded successfully
    if image is not None:
        st.image(image, caption='Original Image', use_column_width=True)

        # Adjust contrast and brightness
        alpha = st.slider('Contrast', 0.1, 3.0, 1.0)
        beta = st.slider('Brightness', -100, 100, 0)
        contrast_brightness_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        st.image(contrast_brightness_image, caption='Contrast and Brightness Adjusted', use_column_width=True)

        # Apply smoothing (blurring)
        smoothed_image = cv2.GaussianBlur(contrast_brightness_image, (5, 5), 0)
        st.image(smoothed_image, caption='Smoothened Image', use_column_width=True)

        # Apply sharpening
        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])
        sharpened_image = cv2.filter2D(smoothed_image, -1, kernel)
        st.image(sharpened_image, caption='Sharpened Image', use_column_width=True)

        # Create a binary mask for masking
        gray_image = cv2.cvtColor(contrast_brightness_image, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

        # Apply morphological operation (dilation)
        kernel = np.ones((5, 5), np.uint8)
        masked_image = cv2.bitwise_and(sharpened_image, sharpened_image, mask=mask)
        dilated_image = cv2.dilate(masked_image, kernel, iterations=1)
        st.image(dilated_image, caption='Masked and Dilated Image', use_column_width=True)