import fitz  # PyMuPDF
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
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

if __name__ == "__main__":
    pdf_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\health.pdf"
    text = extract_text_from_pdf(pdf_path)
    print(text)

def clean_text(text):
    # Remove unnecessary whitespace and special characters
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s,.?!]', '', text)
    return text

def split_into_paragraphs(text):
    paragraphs = text.split('\n\n')
    return [p.strip() for p in paragraphs if p.strip()]

def split_custom_sections(text, delimiter):
    sections = text.split(delimiter)
    return [s.strip() for s in sections if s.strip()]

def vectorize_sections(sections):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sections)
    return vectors

def preprocess_text(text, section_delimiter=None):
    # Step 1: Clean text
    cleaned_text = clean_text(text)
    
    # Step 2: Split text into sections
    if section_delimiter:
        sections = split_custom_sections(cleaned_text, section_delimiter)
    else:
        sections = split_into_paragraphs(cleaned_text)
    
    # Step 3: Vectorize sections
    vectors = vectorize_sections(sections)
    
    return vectors, sections

if __name__ == "__main__":
    pdf_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\health.pdf"
    text = extract_text_from_pdf(pdf_path)
    
    # Preprocess the text, assuming paragraphs as default sections
    vectors, sections = preprocess_text(text)
    
    # Optionally, split the text into custom sections based on delimiter (e.g., "## Page")
    custom_vectors, custom_sections = preprocess_text(text, section_delimiter="## Page")
    
    print(sections)  # Print sections to verify
