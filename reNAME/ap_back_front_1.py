import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline
import os
import re

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

def clean_answer(question, answer):
    if "name" in question.lower():
        match = re.search(r"Name\s*—\s*([A-Za-z\s]+)", answer)
        result = match.group(1).strip() if match else answer
    elif "limit" in question.lower():
        match = re.search(r"Limit\s*-\s*(\$\d{1,3}(,\d{3})*(\.\d{2})?)", answer)
        result = match.group(1).strip() if match else answer
    elif "company" in question.lower() and "underwriting" not in question.lower():
        match = re.search(r"Company\s*—\s*([A-Za-z\s]+)", answer)
        result = match.group(1).strip() if match else answer
    elif "underwriting company" in question.lower():
        match = re.search(r"Underwriting Company\s*—\s*([A-Za-z\s]+)", answer)
        result = match.group(1).strip() if match else answer
    else:
        result = answer.strip()
    
    # Remove any characters not allowed in filenames
    result = re.sub(r'[<>:"/\\|?*\n]', '', result)
    return result

def rename_and_save_pdf(pdf_file, new_name):
    # Ensure the new name doesn't contain any invalid characters
    new_name = re.sub(r'[<>:"/\\|?*\n]', '', new_name)
    os.rename(pdf_file, new_name)

# Streamlit app
st.title("PDF Renaming App")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    extracted_text = extract_text_from_pdf("temp.pdf")
    name = get_answer_from_text(extracted_text, "What is the name?")
    limit = get_answer_from_text(extracted_text, "What is the limit?")
    company = get_answer_from_text(extracted_text, "What is the company name?")
    underwriting_company = get_answer_from_text(extracted_text, "What is the underwriting company name?")
    
    name = clean_answer("name", name)
    limit = clean_answer("limit", limit)
    company = clean_answer("company", company)
    underwriting_company = clean_answer("underwriting company", underwriting_company)
    
    new_name = f"{name} {limit} {company} {underwriting_company}.pdf"
    rename_and_save_pdf("temp.pdf", new_name)
    
    st.success(f"File renamed to: {new_name}")
    st.download_button(
        label="Download renamed PDF",
        data=open(new_name, "rb").read(),
        file_name=new_name,
        mime="application/pdf"
    )
