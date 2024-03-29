import streamlit as st
from PIL import Image
import numpy as np
import cv2

### Sidebar ###

# Logo
app_logo = Image.open("./Images/logo.png")
st.sidebar.image(app_logo)

# Image Upload
st.sidebar.subheader("Image Upload:")
uploaded_file = st.sidebar.file_uploader(
    "Choose an image from your local directory...",
    type=["jpg", "jpeg", "png", "bmp"]
)

# Thresholds
st.sidebar.subheader("Apply thresholding:")
low_thresh = st.sidebar.number_input(
    "Insert a number for the lower threshold (default=15)."
)
upper_thresh = st.sidebar.number_input(
    "Insert a number for the upper threshold (default=200)."
)

# Detect edges button
edge_button = st.sidebar.button("Detect edges")


### Main App ###

# Main title
st.title("Edge Detection Application (v0.1.0)")

# App development info
st.markdown(
    "Application made by [Christos Gkoumas]"
    "(https://github.com/n3urovirtual)."
)

# Original image
if uploaded_file is None:
    image = Image.open("./Images/demo_img.JPG")
    st.image (image, caption="Demo Image", use_column_width=True)
else:
    image = Image.open(uploaded_file)
    st.image (image, caption="Uploaded Image", use_column_width=True)

# Edge Image
if edge_button:
    array = np.asarray(image)
    gray = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    blurry = cv2.GaussianBlur(gray, (5, 5), 0)
    if low_thresh == 0 and upper_thresh == 0:
        edged = cv2.Canny(blurry, 15, 200)
    else:
        edged = cv2.Canny(blurry, low_thresh, upper_thresh)
    st.image(edged, caption="Edge Image", use_column_width=True)

    # Download button
    im = Image.fromarray(edged)
    im.save("Edge_image.png")
    with open("Edge_image.png", "rb") as file:
        btn = st.download_button(
                 label="Download Image",
                 data=file,
                 file_name="Edge_image.png",
                 mime="image/png"
               )
