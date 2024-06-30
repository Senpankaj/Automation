import os
import fitz  # PyMuPDF
from transformers import AutoModelForCausalLM, AutoTokenizer
import streamlit as st

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to query the model with rules
def query_model_with_rules(prompt, model, tokenizer, rules, max_length=1024):
    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Apply rules to the generated text
    for rule in rules:
        generated_text = rule(generated_text)
    
    return generated_text

# Example rule to ensure the response contains a specific keyword
def must_contain_keyword(keyword):
    def rule(text):
        if keyword in text:
            return text
        return f"The response does not contain the required keyword: {keyword}"
    return rule

# Load the pre-trained model and tokenizer
model_name = "EleutherAI/gpt-neo-2.7B"  # or "EleutherAI/gpt-j-6B" for GPT-J
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Static PDF file path
static_pdf_path = "C:/Users/AdminT/Desktop/pdf/3.pdf"

# Extract text from the static PDF
pdf_text = extract_text_from_pdf(static_pdf_path)

# Define your rules
rules = [must_contain_keyword("specific information")]

# Generate response based on a prompt with rules
prompt = "Summarize the following text: " + pdf_text
response = query_model_with_rules(prompt, model, tokenizer, rules)

# Print the response and rename the PDF
print(f"Summary: {response}")
new_name = response.replace(" ", "_")[:50] + ".pdf"
new_path = os.path.join(os.path.dirname(static_pdf_path), new_name)
os.rename(static_pdf_path, new_path)
print(f"Renamed PDF to: {new_name}")

# Streamlit app
st.title("PDF Processor with GPT-Neo/J")

uploaded_files = st.file_uploader("Choose PDFs", accept_multiple_files=True, type=["pdf"])

if uploaded_files:
    for uploaded_file in uploaded_files:
        with st.spinner(f"Processing {uploaded_file.name}"):
            # Save the uploaded file
            file_path = os.path.join("uploads", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Extract text from the PDF
            pdf_text = extract_text_from_pdf(file_path)

            # Generate response based on a prompt with rules
            prompt = "Summarize the following text: " + pdf_text
            response = query_model_with_rules(prompt, model, tokenizer, rules)

            # Display the response
            st.write(f"Summary for {uploaded_file.name}:")
            st.write(response)

            # Rename the PDF based on the response
            new_name = response.replace(" ", "_")[:50] + ".pdf"
            new_path = os.path.join("uploads", new_name)
            os.rename(file_path, new_path)
            st.write(f"Renamed PDF: {new_name}")
