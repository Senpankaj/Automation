from PyPDF2 import PdfReader
from transformers import pipeline

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def get_answer_from_text(text, question):
    qa_pipeline = pipeline("question-answering", model="distilbert/distilbert-base-cased-distilled-squad", revision="626af31")
    answer = qa_pipeline(question=question, context=text)
    return answer['answer'].strip()

# Test the functions
sample_pdf_file = "Name.pdf"  # Change this to your PDF filename
extracted_text = extract_text_from_pdf(sample_pdf_file)
name = get_answer_from_text(extracted_text, "What is the name?")
limit = get_answer_from_text(extracted_text, "What is the limit?")
company = get_answer_from_text(extracted_text, "What is the company name?")
underwriting_company = get_answer_from_text(extracted_text, "What is the underwriting company name?")
print(f"Name: {name}")
print(f"Limit: {limit}")
print(f"Company: {company}")
print(f"Underwriting Company: {underwriting_company}")
