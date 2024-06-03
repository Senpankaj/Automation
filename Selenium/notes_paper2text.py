import cv2
import pytesseract
from PIL import Image
import numpy as np

# Function to preprocess the image
def preprocess_image(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply adaptive thresholding to binarize the image
    processed_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    return processed_img

# Function to recognize text using Tesseract OCR
def recognize_text(processed_img):
    # Convert image to PIL format
    pil_img = Image.fromarray(processed_img)
    
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(pil_img)
    
    return text

# Main function to convert handwritten notes to text
def handwritten_to_text(image_path):
    # Preprocess the image
    processed_img = preprocess_image(image_path)
    
    # Recognize text from the preprocessed image
    text = recognize_text(processed_img)
    
    return text

# Example usage
image_path = 'handwritten_notes.jpg'  # Path to the image file
text = handwritten_to_text(image_path)
print(text)
