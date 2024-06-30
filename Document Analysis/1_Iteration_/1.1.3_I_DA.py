import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Corrected file path
pdf_path = r"C:\Users\AdminT\Documents\Automation\Automation\Document Analysis\Research Papers\13.pdf"
text = extract_text_from_pdf(pdf_path)
#print(text)

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

preprocessed_text = preprocess_text(text)
print(preprocessed_text)

from transformers import pipeline

# Load pre-trained model
qa_pipeline = pipeline("question-answering")    

# Example question-answering
context = "Your extracted text from the PDF."
question = "what is the summary of the section introduction?"
result = qa_pipeline(question=question, context=context)
print(result)
