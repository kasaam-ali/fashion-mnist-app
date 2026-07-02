import streamlit as st
import requests
import io
from PIL import Image
import os

st.set_page_config(page_title="Fashion MNIST Classifier", page_icon="👕", layout="centered")

st.title("👕 Fashion MNIST Classification")
st.write("Upload an image of a clothing item (T-shirt, Trouser, Sneaker, etc.) to classify it!")

API_URL = "https://kasaam89-fashion-mnist.hf.space/predict"

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.write("🔄 Classifying...")

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()

    try:
        headers = {"Accept": "application/json"}
        files = {
            "file": (uploaded_file.name, img_byte_arr, "image/png")
        }

        response = requests.post(
            API_URL,
            files=files,
            headers=headers,
            timeout=20
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"### 🎉 Prediction: **{result['predicted_class']}**")
            st.metric(
                label="Confidence Score",
                value=f"{result['confidence'] * 100:.2f}%"
            )
        else:
            st.error(f"Error: Server responded with status code {response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server. Make sure your backend is running.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
