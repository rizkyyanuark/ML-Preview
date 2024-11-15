import requests
import os
import io
from dotenv import load_dotenv
import streamlit as st

api_model = "http://localhost:8000"


@st.cache_data
def default():
    response = requests.get(api_model)

    if response.status_code == 200:
        # data = response.json()
        return response.text
    else:
        data = "An error occurred:", response.status_code
        return data


@st.cache_data
def predict(image):
    url = api_model + "/predict_image"  # Sesuaikan endpoint jika perlu

    # Siapkan file image sesuai dengan format di API
    files = {"image": ("image.jpg", io.BytesIO(image), "image/jpeg")}
    headers = {}

    # Kirim request POST ke API
    response = requests.post(url, headers=headers, files=files)

    # Pastikan bahwa respons dalam format JSON, lalu akses prediksi
    if response.status_code == 200:
        result = response.json()
        predicted_class = result["data"]["predicted_class"]
        confidence = result["data"]["confidence"]

        # Tampilkan hasil prediksi
        return predicted_class, confidence
    else:
        # Tampilkan pesan error jika ada
        return f"Error: {response.status_code} - {response.text}"
