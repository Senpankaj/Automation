import streamlit as st
import os
from PyPDF2 import PdfReader
from transformers import pipeline

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to rename PDF based on extracted information
def rename_pdf(pdf_file):
    text = extract_text_from_pdf(pdf_file)
    if not text:
        st.error("Failed to extract text from PDF. Please ensure the PDF is not empty or corrupted.")
        return None
    # Use Hugging Face transformers pipeline for question answering
    qa_pipeline = pipeline("question-answering")
    question = "What is the name and company?"
    answer = qa_pipeline(question=question, context=text)
    if not answer['answer']:
        st.error("Failed to extract name and company from PDF. Please check the content of the PDF.")
        return None
    # Extract name and company from the answer
    name = answer['answer']
    limit = "Limit 1"  # You mentioned a fixed string for limit 1
    company = "Company"  # Replace with extracted company name
    new_name = f"{name} {limit} {company}.pdf"
    os.rename(pdf_file, new_name)
    return new_name

# Streamlit UI
def main():
    st.title("PDF File Renamer")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        if st.button("Process File"):
            new_file_name = rename_pdf(uploaded_file.name)
            if new_file_name:
                st.write(f"File renamed to: {new_file_name}")

                st.write("Download the processed file:")
                st.download_button(
                    label="Download Processed File",
                    data=open(new_file_name, 'rb').read(),
                    file_name=new_file_name
                )

if __name__ == "__main__":
    main()
