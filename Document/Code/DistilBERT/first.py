import fitz  # PyMuPDF for reading PDFs
from transformers import pipeline

# Function to extract text from PDF using PyMuPDF
def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Function to extract author's name using DistilBERT for question answering
def extract_author_name(text):
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    question = "What is the title of the research paper?"
    answer = qa_pipeline(question=question, context=text)
    return answer['answer']

# Main function to process PDF and extract author's name
def extract_author_from_pdf(pdf_path):
    try:
        text = extract_text_from_pdf(pdf_path)
        author_name = extract_author_name(text)
        return author_name
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Example usage
pdf_path = r"C:\Users\AdminT\Desktop\pdf\2.pdf"
author_name = extract_author_from_pdf(pdf_path)

if author_name:
    print(f"The title of the research paper is: {author_name}")
else:
    print("Unable to determine the author.")
