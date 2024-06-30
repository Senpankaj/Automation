import fitz  # PyMuPDF
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from transformers import pipeline

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

# Function to preprocess text data
def preprocess_text(text):
    try:
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        
        tokens = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return tokens
    except Exception as e:
        print(f"Error preprocessing text: {e}")
        return []

# Load pre-trained model
try:
    qa_pipeline = pipeline("question-answering")
except Exception as e:
    print(f"Error loading QA pipeline: {e}")
    qa_pipeline = None

# Main script
pdf_path = r"C:\Users\AdminT\Documents\Automation\Automation\Document Analysis\Research Papers\13.pdf"
text = extract_text_from_pdf(pdf_path)
print("Extracted text:", text[:500])  # Print the first 500 characters of the extracted text for debugging

preprocessed_text = preprocess_text(text)
print("Preprocessed text:", preprocessed_text[:50])  # Print the first 50 tokens for debugging

context = " ".join(preprocessed_text)
print("Context length:", len(context.split()))

# Example question-answering
if qa_pipeline:
    question = "Gve summary of the section Indroduction?"
    try:
        result = qa_pipeline(question=question, context=context)
        print("QA result:", result)
    except Exception as e:
        print(f"Error during question-answering: {e}")
else:
    print("QA pipeline not initialized.")
