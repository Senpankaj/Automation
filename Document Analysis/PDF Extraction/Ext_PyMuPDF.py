import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path, output_md_path):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    with open(output_md_path, 'w', encoding='utf-8') as md_file:
        md_file.write("# Extracted Text\n\n")

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text = page.get_text("text")

            md_file.write(f"## Page {page_num + 1}\n")
            md_file.write("```\n")
            md_file.write(text)
            md_file.write("\n```\n\n")

if __name__ == "__main__":
    pdf_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\health.pdf"
    output_md_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\health.md"
    extract_text_from_pdf(pdf_path, output_md_path)
