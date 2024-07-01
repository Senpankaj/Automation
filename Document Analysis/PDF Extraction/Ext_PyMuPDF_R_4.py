import fitz  # PyMuPDF
import re
import os

# Step 1: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    extracted_text = "# Extracted Text\n\n"

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")
        extracted_text += f"## Page {page_num + 1}\n"
        extracted_text += text + "\n\n"
        
    return extracted_text

# Step 2: Clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s,.?!\n]', '', text)
    return text

# Step 3: Split text into paragraphs while preserving the context
def split_into_paragraphs(text):
    paragraphs = text.split('\n\n')
    return [p.strip() for p in paragraphs if p.strip()]

# Step 4: Vectorize sections (for machine learning use)
def vectorize_sections(sections):
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sections)
    return vectors

# Step 5: Preprocess text
def preprocess_text(text):
    cleaned_text = clean_text(text)
    paragraphs = split_into_paragraphs(cleaned_text)
    vectors = vectorize_sections(paragraphs)
    return vectors, paragraphs

# Step 6: Save preprocessed text to a .md file
def save_to_md_file(sections, output_md_path):
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as md_file:
        md_file.write("# Preprocessed Text\n\n")
        for i, section in enumerate(sections):
            md_file.write(f"## Section {i + 1}\n")
            md_file.write(section + "\n\n")

# Main function
if __name__ == "__main__":
    pdf_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\health.pdf"
    output_md_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\preprocessed_health.md"
    
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Preprocess the text, preserving paragraphs
    vectors, paragraphs = preprocess_text(text)
    
    # Save preprocessed text to a .md file
    save_to_md_file(paragraphs, output_md_path)
    
    print(f"Preprocessed text saved to {output_md_path}")
