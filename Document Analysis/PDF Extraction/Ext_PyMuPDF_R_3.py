import fitz  # PyMuPDF
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Step 1: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    extracted_text = "# Extracted Text\n\n"

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")
        extracted_text += f"## Page {page_num + 1}\n"
        extracted_text += "```\n"
        extracted_text += text
        extracted_text += "\n```\n\n"

    return extracted_text

# Step 2: Clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s,.?!]', '', text)
    return text

# Step 3: Split text into sections
def split_into_paragraphs(text):
    paragraphs = text.split('\n\n')
    return [p.strip() for p in paragraphs if p.strip()]

def split_custom_sections(text, delimiter):
    sections = text.split(delimiter)
    return [s.strip() for s in sections if s.strip()]

# Step 4: Vectorize sections
def vectorize_sections(sections):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sections)
    return vectors

# Step 5: Preprocess text
def preprocess_text(text, section_delimiter=None):
    cleaned_text = clean_text(text)
    if section_delimiter:
        sections = split_custom_sections(cleaned_text, section_delimiter)
    else:
        sections = split_into_paragraphs(cleaned_text)
    vectors = vectorize_sections(sections)
    return vectors, sections

# Step 6: Save preprocessed text to a .md file
def save_to_md_file(sections, output_md_path):
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as md_file:
        md_file.write("# Preprocessed Text\n\n")
        for i, section in enumerate(sections):
            md_file.write(f"## Section {i + 1}\n")
            md_file.write("```\n")
            md_file.write(section)
            md_file.write("\n```\n\n")

# Main function
if __name__ == "__main__":
    pdf_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\health.pdf"
    output_md_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\preprocessed_health.md"
    
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Preprocess the text, assuming paragraphs as default sections
    vectors, sections = preprocess_text(text)
    
    # Save preprocessed text to a .md file
    save_to_md_file(sections, output_md_path)
    
    print(f"Preprocessed text saved to {output_md_path}")
