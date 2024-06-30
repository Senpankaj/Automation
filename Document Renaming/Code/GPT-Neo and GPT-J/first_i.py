import fitz  # PyMuPDF
from transformers import AutoModelForCausalLM, AutoTokenizer

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to query the model
def query_model(prompt, model, tokenizer, max_length=1024):
    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Load the pre-trained model and tokenizer
model_name = "EleutherAI/gpt-neo-2.7B"  # or "EleutherAI/gpt-j-6B" for GPT-J
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Path to the PDF file
pdf_path = "C:/Users/AdminT/Desktop/pdf/3.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Generate a response based on the extracted text
prompt = "Summarize the following text: " + pdf_text
response = query_model(prompt, model, tokenizer)

# Print the response
print(f"Summary: {response}")
