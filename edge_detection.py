import streamlit as st
from PIL import Image
import numpy as np
import cv2

def read_image(dir, caption=None, column_width=True):
    read_image.image = Image.open(dir)
    st.image(read_image.image, caption=caption, use_column_width=column_width)


### Sidebar ###

# Logo
app_logo = Image.open("./Logos/logo.png")
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
edge_button = st.sidebar.button("Click to detect edges")

# App development info
st.sidebar.markdown(
    "Application made by Christos Gkoumas" 
    "([@n3uro_virtual](https://twitter.com/n3uro_virtual)). Version: 0.1.0"
)


### Main App ###

# Main title
st.title("Edge Detection Application")

# Original image
if uploaded_file is None:
    image = Image.open("demo_img.JPG")
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
    