from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Test the function
sample_pdf_file = "Name.pdf"  # Change this to your PDF filename
extracted_text = extract_text_from_pdf(sample_pdf_file)
print(extracted_text)
