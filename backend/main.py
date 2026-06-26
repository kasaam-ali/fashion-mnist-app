from fastapi import FastAPI,UploadFile,File
from tensorflow import keras
import numpy as np
from PIL import Image
import io
MODEL_PATH = 'fashion.mnist.keras'
model=keras.models.load_model(MODEL_PATH)
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
app=FastAPI()
@app.get("/")
def home():
    return {"message":"API is Working"}
@app.post("/predict")
async def predict(file:UploadFile=File(...)):
    image_bytes= await file.read()
    image=Image.open(io.BytesIO(image_bytes))
    image=image.convert('L')
    image=image.resize((28,28))
    image_array=np.array(image)
    image_array=image_array.reshape(1,28,28)
    image_array=image_array.astype('float32')/255.0
    prediction=model.predict(image_array)
    predicted_index=np.argmax(prediction[0])
    predicted_class=class_names[predicted_index]
    confidence=float(np.max(prediction[0]))
    return {'predicted_class':predicted_class,'confidence':confidence}