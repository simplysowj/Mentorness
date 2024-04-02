import streamlit as st
import cv2
from PIL import Image
import numpy as np
import streamlit as st
from PIL import Image
import torchvision.transforms as transforms
from torchvision.models import resnet50
import torch
import torch.nn.functional as F
import requests
from io import BytesIO
import tensorflow as tf
import numpy as np
from PIL import Image


# Load the pre-trained model
#model = tf.keras.applications.InceptionV3(include_top=False, weights='imagenet')
#new_input = model.input
#hidden_layer = model.layers[-1].output
#model = tf.keras.Model(new_input, hidden_layer)


# Load the tokenizer
#tokenizer = tf.keras.preprocessing.text.Tokenizer()
#tokenizer_path = "tokenizer.json"  # Path to your tokenizer file
#tokenizer_config = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_path)

# Load the pre-trained captioning model
#caption_model = tf.keras.models.load_model("caption_model.h5")

# Define the maximum sequence length
max_length = 100
def load_image(image_path):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, (299, 299))
    img = tf.keras.applications.inception_v3.preprocess_input(img)
    return img

def generate_caption(image_path):
    img = load_image(image_path)
    img = np.expand_dims(img, axis=0)
    feature_vector = model.predict(img)

    start_token = tokenizer_config.word_index["<start>"]
    end_token = tokenizer_config.word_index["<end>"]

    caption = [start_token]
    for i in range(max_length):
        sequence = tf.convert_to_tensor([caption])
        predictions = caption_model.predict([feature_vector, sequence])
        predicted_id = np.argmax(predictions, axis=2)
        if predicted_id == end_token:
            break
        caption.append(predicted_id)

    caption = tokenizer_config.sequences_to_texts([caption])[0]
    return caption



def painting_effect(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Invert the grayscale image
    inverted_gray_image = 255 - gray_image
    # Apply bilateral filter to the inverted grayscale image
    bilateral_filtered_image = cv2.bilateralFilter(inverted_gray_image, 11, 17, 17)
    # Invert the bilateral filtered image
    inverted_filtered_image = 255 - bilateral_filtered_image
    # Create the painting effect by blending the inverted filtered image with the original image
    painting_image = cv2.bitwise_and(image, image, mask=inverted_filtered_image)
    return painting_image

def pencil_sketch(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Invert the grayscale image
    inverted_gray_image = 255 - gray_image
    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    # Invert the blurred image
    inverted_blurred_image = 255 - blurred_image
    # Create the pencil sketch image by blending the inverted blurred image with the grayscale image
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    return pencil_sketch_image

# Display a file uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)
    # Convert the image to a format compatible with OpenCV
    opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # Perform pencil sketch conversion
    sketch_image = pencil_sketch(opencv_image)
    # Display the original and sketch images
    st.image([image, sketch_image], caption=['Original Image', 'Pencil Sketch'], width=300)

    # Perform painting effect conversion
    painting_image = painting_effect(opencv_image)
    # Display the original and painting images
    st.image([image, painting_image], caption=['Original Image', 'Painting Effect'], width=300)

    

    
