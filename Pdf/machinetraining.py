from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define functions to extract text from PDF and get labels
def extract_text(pdf_path):
  # Use libraries like PyPDF2 to extract text from PDF
  # ... (implementation details)
  return extracted_text

def get_label(pdf_path):
  # Define logic to assign labels based on naming convention or file location
  # ... (implementation details)
  return label

# Load your PDFs and labels
pdf_paths = [path1, path2, ...]  # List of PDF paths
labels = [get_label(path) for path in pdf_paths]

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(pdf_paths, labels, test_size=0.2)

# Feature extraction: convert PDFs to TF-IDF vectors
vectorizer = TfidfVectorizer()
X_train_features = vectorizer.fit_transform([extract_text(path) for path in X_train])
X_test_features = vectorizer.transform([extract_text(path) for path in X_test])

# Train a Multinomial Naive Bayes model
model = MultinomialNB()
model.fit(X_train_features, y_train)

# Save the trained model (using libraries like pickle)
import pickle
pickle.dump(model, open("pdf_classifier.sav", "wb"))
pickle.dump(vectorizer, open("vectorizer.sav", "wb"))

print("Model training complete!")
