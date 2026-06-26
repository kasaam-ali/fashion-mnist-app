import streamlit as st
import requests
from PIL import Image
import io

# Page Configuration
st.set_page_config(page_title="Fashion MNIST Classifier", layout="centered")

st.title("👕 Fashion MNIST Classification")
st.write("Upload an image of a clothing item (T-shirt, Trouser, Sneaker, etc.) to classify it!")

# FastAPI endpoint URL
API_URL = "http://127.0.0.1:8000/predict"

# File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    st.write("Classifying...")
    
    # Convert image to bytes for sending via API
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format=image.format if image.format else 'JPEG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Prepare files dictionary for multipart/form-data
    files = {"file": (uploaded_file.name, img_byte_arr, uploaded_file.type)}
    
    try:
        # Send POST request to FastAPI backend
        response = requests.post(API_URL, files=files)
        
        if response.status_code == 200:
            result = response.json()
            
            # Extract data from response
            prediction = result["predicted_class"]
            confidence = result["confidence"] * 100
            
            # Show Results in a nice format
            st.success(f"**Prediction:** {prediction}")
            st.info(f"**Confidence:** {confidence:.2f}%")
        else:
            st.error(f"Error from API server: Status Code {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server. Make sure your backend is running on http://127.0.0.1:8000")