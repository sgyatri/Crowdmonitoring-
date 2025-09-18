# app.py
import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="CSRNet Crowd Counting Demo", layout="wide")

st.title("CSRNet Crowd Counting Demo (Colab + Cloudflare)")
st.write("Upload an image and I'll (pretend to) estimate the crowd. Replace the dummy estimator with CSRNet model code later.")

uploaded_file = st.file_uploader("Upload an image (jpg/png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and show the image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_column_width=True)

    # Dummy "estimation" — replace with your model inference
    estimated_count = np.random.randint(50, 500)
    st.success(f"Estimated crowd count: {estimated_count}")

    # Optional: show a small histogram / density placeholder
    st.subheader("Dummy density preview")
    st.bar_chart({"Density bins": np.random.randint(0, 50, size=8)})
else:
    st.info("Please upload an image to start crowd counting.")


