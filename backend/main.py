from pathlib import Path
import io

from fastapi import FastAPI, UploadFile, File
from PIL import Image
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "fashion.mnist.keras"

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def train_and_save_model(model_path: Path):
    (x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
    
    # CNN ke liye (28, 28, 1) mein reshape kiya
    x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    
    # CNN Architecture
    model = keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(10, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Epochs 3 se badha kar 10 kar diye
    model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))
    model.save(model_path)
    return model

def load_model():
    if MODEL_PATH.exists():
        return keras.models.load_model(MODEL_PATH)
    return train_and_save_model(MODEL_PATH)

model = load_model()

@app.get("/")
def home():
    return {"message": "API is Working"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image)
    
    # Prediction ke liye bhi (1, 28, 28, 1) zaroori hai
    image_array = image_array.reshape(1, 28, 28, 1)
    image_array = image_array.astype('float32') / 255.0
    
    prediction = model.predict(image_array)
    predicted_index = np.argmax(prediction[0])
    predicted_class = class_names[predicted_index]
    confidence = float(np.max(prediction[0]))
    
    return {'predicted_class': predicted_class, 'confidence': confidence}
