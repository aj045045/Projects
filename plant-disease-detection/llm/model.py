import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("./assets/best_grayscale_model.keras")

infer = load_model()

def preprocess_image(image_path):
    image = Image.open(image_path).convert("L")  # Grayscale
    image = image.resize((224, 224))
    image = np.array(image) / 255.0              # Shape: (224, 224)
    image = np.expand_dims(image, axis=-1)       # Add channel: (224, 224, 1)
    image = np.expand_dims(image, axis=0)        # Add batch: (1, 224, 224, 1)
    return image.astype(np.float32)

# Predict
def predict_disease_tf(image_path):
    image = preprocess_image(image_path)
    input_tensor = tf.convert_to_tensor(image)
    output = infer.predict(input_tensor)
    predicted = np.argmax(output, axis=1)[0]

    # disease_classes = ['Apple___Scab', 'Apple___Black_rot', 'Corn___Blight']
    disease_classes = [
        'Apple___Apple_scab',
        'Apple___Black_rot',
        'Apple___Cedar_apple_rust',
        'Apple___healthy',
        'Blueberry___healthy',
        'Cherry_(including_sour)___Powdery_mildew',
        'Cherry_(including_sour)___healthy',
        'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
        'Corn_(maize)___Common_rust_',
        'Corn_(maize)___Northern_Leaf_Blight',
        'Corn_(maize)___healthy',
        'Grape___Black_rot',
        'Grape___Esca_(Black_Measles)',
        'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
        'Grape___healthy',
        'Orange___Haunglongbing_(Citrus_greening)',
        'Peach___Bacterial_spot',
        'Peach___healthy',
        'Pepper,_bell___Bacterial_spot',
        'Pepper,_bell___healthy',
        'Potato___Early_blight',
        'Potato___Late_blight',
        'Potato___healthy',
        'Raspberry___healthy',
        'Soybean___healthy',
        'Squash___Powdery_mildew',
        'Strawberry___Leaf_scorch',
        'Strawberry___healthy',
        'Tomato___Bacterial_spot',
        'Tomato___Early_blight',
        'Tomato___Late_blight',
        'Tomato___Leaf_Mold',
        'Tomato___Septoria_leaf_spot',
        'Tomato___Spider_mites Two-spotted_spider_mite',
        'Tomato___Target_Spot',
        'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
        'Tomato___Tomato_mosaic_virus',
        'Tomato___healthy'
        ]
    return disease_classes[predicted]
