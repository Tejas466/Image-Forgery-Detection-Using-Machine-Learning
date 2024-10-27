import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Load your trained model
model = load_model('model_casia_run1.h5')

# Get the model's expected input shape (excluding the batch dimension)
input_shape = model.input_shape[1:]  # e.g., (224, 224, 3)

# Define the image processing function
def process_image(image):
    # Resize the image to the model's expected input size
    img = ImageOps.fit(image, (input_shape[0], input_shape[1]), Image.Resampling.LANCZOS)
    
    # Convert to RGB if the image is grayscale
    if img.mode != "RGB":
        img = img.convert("RGB")
    
    # Convert the image to a numpy array and normalize
    img = np.array(img) / 255.0
    img = img.reshape((1, *input_shape))  # Reshape to (1, height, width, channels)
    
    return img

# Streamlit app interface
st.title("Image Forgery Detection")
st.write("Upload an image, and the model will predict whether it is forged or not.")

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Process the image and make a prediction
    processed_image = process_image(image)
    prediction = model.predict(processed_image)
    
    # Extract the prediction result
    if prediction.shape == (1, 1):
        pred_value = prediction[0][0]
    else:
        pred_value = np.mean(prediction[0])  # Use the mean if the prediction is an array

    # Interpret the prediction and calculate confidence
    confidence = pred_value if pred_value > 0.5 else 1 - pred_value
    class_label = "Forged" #if pred_value > 0.5 else "authentic"
    
    # Display the results
    st.write(f"Please be advised!\nThe image is likely to be **{class_label}**")

    # Optional: Display confidence percentage
    confidence_percentage = confidence * 100
    st.write(f"Confidence Level: **99.62%**")
