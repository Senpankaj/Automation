import PyPDF2
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import torch

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        first_page = reader.pages[0]
        text = first_page.extract_text()
    return text

def get_title_from_text(text, model, tokenizer):
    prompt = "Extract the title of the research paper from the following text:\n\n" + text
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True, max_length=1024)
    
    outputs = model.generate(
        inputs.input_ids, 
        attention_mask=inputs.attention_mask,
        max_new_tokens=50,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id  # Ensuring proper padding
    )
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    title = generated_text.split('\n')[0]
    return title

def main(pdf_path):
    text = read_pdf(pdf_path)
    
    model_name = "EleutherAI/gpt-neo-1.3B"
    model = GPTNeoForCausalLM.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    
    # Add padding token if it doesn't exist
    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({'pad_token': tokenizer.eos_token})
        model.resize_token_embeddings(len(tokenizer))

    title = get_title_from_text(text, model, tokenizer)
    return title

if __name__ == "__main__":
    pdf_path = r"C:\Users\AdminT\Desktop\pdf\2.pdf"
    title = main(pdf_path)
    print(f"Title of the research paper: {title}")
