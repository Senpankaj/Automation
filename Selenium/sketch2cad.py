import cv2
import numpy as np
import ezdxf
import joblib  # Corrected import for joblib

# Function to preprocess the image
def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Apply edge detection
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    return edges

# Function to extract features from the preprocessed image
def extract_features(edges):
    # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    features = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        features.append(approx)
    return features

# Function to recognize shapes using a pre-trained model
def recognize_shapes(features, model):
    recognized_shapes = []
    for feature in features:
        # Feature extraction logic (this is a placeholder)
        shape_type = model.predict([feature.flatten()])
        recognized_shapes.append(shape_type)
    return recognized_shapes

# Function to create a DXF file from recognized shapes
def create_dxf(recognized_shapes, output_file):
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()
    
    for shape in recognized_shapes:
        if shape[0] == 'circle':
            center, radius = (shape[1][0], shape[1][1]), shape[1][2]  # Example format
            msp.add_circle(center, radius)
        elif shape[0] == 'line':
            start_point, end_point = shape[1][0], shape[1][1]  # Example format
            msp.add_line(start_point, end_point)
        # Add more shapes as necessary
    
    doc.saveas(output_file)

# Main function to scan, recognize, and create DXF file
def main(image_path, model_path, output_file):
    edges = preprocess_image(image_path)
    features = extract_features(edges)
    model = joblib.load(model_path)
    recognized_shapes = recognize_shapes(features, model)
    create_dxf(recognized_shapes, output_file)

if __name__ == '__main__':
    image_path = '12.jpeg'
    model_path = 'sketch_recognition_model.pkl'
    output_file = 'cad.dwg'
    main(image_path, model_path, output_file)
