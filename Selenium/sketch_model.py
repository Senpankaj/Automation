import numpy as np
from sklearn.svm import SVC
import joblib

# Generate synthetic data: 100 circles and 100 lines
def generate_synthetic_data():
    X = []
    y = []
    
    # Circles: (x, y, radius)
    for _ in range(100):
        x, y, radius = np.random.randint(0, 100, size=3)
        X.append([x, y, radius])
        y.append('circle')
    
    # Lines: (x1, y1, x2, y2)
    for _ in range(100):
        x1, y1, x2, y2 = np.random.randint(0, 100, size=4)
        X.append([x1, y1, x2, y2])
        y.append('line')
    
    return np.array(X), np.array(y)

# Train a simple SVM classifier
def train_and_save_model():
    X, y = generate_synthetic_data()
    
    # Verify the shapes of the generated data
    print(f"Generated data shape: X={X.shape}, y={y.shape}")
    
    # Convert the labels to a numeric format if necessary
    unique_labels = np.unique(y)
    label_to_num = {label: num for num, label in enumerate(unique_labels)}
    y_num = np.array([label_to_num[label] for label in y])
    
    # Verify the labels conversion
    print(f"Unique labels: {unique_labels}")
    print(f"Label to number mapping: {label_to_num}")
    
    # Train the model
    model = SVC()
    model.fit(X, y_num)
    
    # Save the model and label mapping
    joblib.dump((model, label_to_num), 'sketch_recognition_model.pkl')
    print("Model saved as 'sketch_recognition_model.pkl'")

if __name__ == '__main__':
    train_and_save_model()
