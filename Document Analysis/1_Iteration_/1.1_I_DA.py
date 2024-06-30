import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

pdf_path = "sample.pdf"
text = extract_text_from_pdf(pdf_path)
print(text)

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
question = "What is the main topic of the text?"
result = qa_pipeline(question=question, context=context)
print(result)

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    text = extract_text_from_pdf(pdf_path)
    context = " ".join(preprocess_text(text))
    
    qa_pipeline = pipeline("question-answering")

    while True:
        question = input("Ask a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        result = qa_pipeline(question=question, context=context)
        print(f"Answer: {result['answer']}")

if __name__ == "__main__":
    main()
