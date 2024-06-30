import PyPDF2
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch

def read_pdf(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # Extract text from the first page
        first_page = reader.pages[0]
        text = first_page.extract_text()
    return text

def get_title_from_text(text, model, tokenizer):
    # Prepare the prompt for the model
    prompt = "Extract the title of the research paper from the following text:\n\n" + text
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generate the response
    outputs = model.generate(inputs.input_ids, max_length=50, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract the title (assuming it's the first line)
    title = generated_text.split('\n')[0]
    return title

def main(pdf_path):
    # Read the PDF file
    text = read_pdf(pdf_path)
    
    # Load the model and tokenizer
    model_name = "EleutherAI/gpt-neo-1.3B"  # or your local model path
    model = GPTNeoForCausalLM.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    
    # Get the title from the text
    title = get_title_from_text(text, model, tokenizer)
    return title

# Example usage
pdf_path = r"C:\Users\AdminT\Desktop\pdf\3.pdf"
title = main(pdf_path)
print(f"Title of the research paper: {title}")
