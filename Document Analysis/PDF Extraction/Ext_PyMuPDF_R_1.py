import fitz  # PyMuPDF

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
