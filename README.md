# 👕 Fashion MNIST Classifier

<div align="center">

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![HuggingFace](https://img.shields.io/badge/🤗%20Hosted%20on-HuggingFace-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/kasaam89/fashion-mnist-front)
[![License MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

**AI-Powered Clothing Classification** | **Live Demo Available** 🚀

[🌐 Try Live Demo](#-live-demo) • [📚 Documentation](#-tech-stack) • [🛠️ Installation](#-getting-started)

</div>

---

## 📋 Overview

A cutting-edge web application that classifies clothing images using a deep learning model trained on the **Fashion MNIST dataset**. Upload an image, and our AI instantly identifies the clothing type with high accuracy! 🎯

**Key Features:**
- 🔥 Real-time image classification
- 🎨 Beautiful Streamlit UI
- ⚡ Fast FastAPI backend
- 🧠 Deep learning powered
- 📱 Responsive design
- ☁️ Cloud-hosted & ready to use

---

## 🌐 Live Demo

🚀 **Try it now:** [Fashion MNIST Classifier - Live](https://huggingface.co/spaces/kasaam89/fashion-mnist-front)

Simply upload a clothing image and get instant predictions!

---

## 🏗️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| 🔧 **Backend** | FastAPI, TensorFlow/Keras | Model inference & API |
| 🎨 **Frontend** | Streamlit | User interface |
| 🧠 **Model** | Fully Connected NN | Deep learning inference |
| 📊 **Framework** | TensorFlow/Keras | ML framework |

**Model Architecture:**
```
Input (28×28) → Flatten → Dense(128) → ReLU → Dense(64) → ReLU → Dense(10) → Softmax
```

---

## 👕 Clothing Classes

The model can classify 10 different clothing types:

| Class | Icon |
|-------|------|
| T-shirt/top | 👔 |
| Trouser | 👖 |
| Pullover | 🧶 |
| Dress | 👗 |
| Coat | 🧥 |
| Sandal | 👡 |
| Shirt | 👕 |
| Sneaker | 👟 |
| Bag | 👜 |
| Ankle boot | 🥾 |

---

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.8+
- pip package manager
- Virtual environment (recommended)

### 1️⃣ Install Dependencies

```bash
pip install fastapi uvicorn tensorflow numpy pillow streamlit requests
```

### 2️⃣ Run the Backend

```bash
cd backend
uvicorn main:app --reload
```

✅ API will be available at `http://localhost:8000`

### 3️⃣ Run the Frontend

```bash
cd frontend
streamlit run app.py
```

🌐 Open `http://localhost:8501` in your browser

---

## 🔌 API Endpoints

### Base URL
```
http://localhost:8000
```

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| 🏥 GET | `/` | Health check |
| 🎯 POST | `/predict` | Upload image & get prediction |

### 📝 Example Request

```bash
curl -X POST -F "file=@image.png" http://localhost:8000/predict
```

### ✅ Example Response

```json
{
  "predicted_class": "Sneaker",
  "confidence": 0.9999
}
```

---

## 📊 Performance Metrics

- **Accuracy:** ~92% on Fashion MNIST test set
- **Model Size:** ~550KB
- **Inference Time:** <50ms per image
- **Supported Input:** PNG, JPG, JPEG (28×28 pixels or auto-resized)

---

## 📂 Project Structure

```
fashion-mnist-app/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── model/
│   │   └── model.h5         # Trained model
│   └── requirements.txt
├── frontend/
│   ├── app.py               # Streamlit app
│   └── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 How It Works

1. 📤 User uploads a clothing image via the Streamlit interface
2. 📮 Image is sent to the FastAPI backend
3. 🧠 Model preprocesses and predicts the clothing type
4. 📊 Confidence score is calculated
5. 🎉 Result is displayed with visualization

---

## 🛠️ Configuration

### Modify Model Architecture

Edit `backend/main.py` to change the model:

```python
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
```

### Adjust API Port

```bash
uvicorn main:app --reload --port 8080
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8000 already in use | `uvicorn main:app --reload --port 8080` |
| Model not loading | Ensure `model.h5` is in the correct path |
| CORS errors | Check FastAPI middleware configuration |
| Image upload fails | Verify image format (PNG/JPG) and size |

---

## 📦 Dependencies

```
fastapi==0.104.0
uvicorn==0.24.0
tensorflow==2.14.0
numpy==1.24.0
pillow==10.0.0
streamlit==1.28.0
requests==2.31.0
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! 

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👤 Author

**Kasaam Ali** 👨‍💻

- 🌐 GitHub: [@kasaam-ali](https://github.com/kasaam-ali)
- 🤗 HuggingFace: [@kasaam89](https://huggingface.co/kasaam89)

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub!

---

## 📞 Contact & Support

- 💬 Open an issue for bug reports
- 💡 Suggest features via GitHub discussions
- 📧 Email for direct inquiries

---

<div align="center">

**Made with ❤️ by Kasaam Ali**

[⬆ Back to Top](#-fashion-mnist-classifier)

</div>
