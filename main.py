import streamlit as st
from PIL import Image, ImageFilter, ImageOps
import cv2
import numpy as np

st.title("Image Filtering App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    filter_option = st.selectbox("Choose a filter", ["None", "Grayscale", "Edge Detection", "Blur", "Invert"])

    if filter_option == "Grayscale":
        image = image.convert("L")
    elif filter_option == "Edge Detection":
        img_cv = np.array(image.convert("RGB"))
        img_gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(img_gray, 100, 200)
        image = Image.fromarray(edges)
    elif filter_option == "Blur":
        image = image.filter(ImageFilter.GaussianBlur(radius=2))
    elif filter_option == "Invert":
        image = ImageOps.invert(image.convert("RGB"))

    st.image(image, caption="Filtered Image", use_column_width=True)
