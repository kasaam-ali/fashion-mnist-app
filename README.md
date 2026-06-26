# Fashion MNIST Classifier

A web application that classifies clothing images using a deep learning model trained on the Fashion MNIST dataset. The app consists of a FastAPI backend for model inference and a Streamlit frontend for image upload and visualization.

## Tech Stack

- **Backend**: FastAPI, TensorFlow/Keras
- **Frontend**: Streamlit
- **Model**: Fully connected neural network (Flatten → Dense 128 → Dense 64 → Dense 10)

## Classes

T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle boot

## Getting Started

### 1. Install dependencies

```bash
pip install fastapi uvicorn tensorflow numpy pillow streamlit requests
```

### 2. Run the backend

```bash
cd backend
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### 3. Run the frontend

```bash
cd frontend
streamlit run app.py
```

Open `http://localhost:8501` in your browser, upload a clothing image, and get a prediction.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/predict` | Upload image and get prediction |

### Example

```bash
curl -X POST -F "file=@image.png" http://localhost:8000/predict
```

Response:

```json
{
  "predicted_class": "Sneaker",
  "confidence": 0.9999
}
```
