import pytesseract
import fitz  # For efficient PDF handling
from io import BytesIO  # For image conversion

def pdf_to_word_ocr(pdf_path, output_path):
    """Converts a PDF to a Word document using OCR while attempting to maintain layout.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_path (str): Path to save the output Word document.
    """

    try:
        # Ensure Tesseract is installed and configured (https://pytesseract.readthedocs.io/en/latest/installation.html)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with your Tesseract path if needed

        doc = fitz.open(pdf_path)

        # Create a new Word document
        word_doc = fitz.open()

        for page_num in range(len(doc)):
            page = doc[page_num]
            image = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Increase matrix for better quality (adjust based on needs)
            image_data = BytesIO()
            image.save(image_data, format="PNG")

            # Perform OCR using Tesseract with potential enhancements for layout preservation (consider experimenting):
            text = pytesseract.image_to_string(image_data, config='--psm 6')  # Experiment with PSM modes (e.g., 6, 10)

            # Extract text formatting information (fonts, sizes, positions) for potential layout recreation (experimental)
            # ... (implementation may involve page layout analysis libraries like Camelot)

            # Create a new page in the Word document
            new_page = word_doc.new_page(width=page.media_box.width, height=page.media_box.height)

            # Insert extracted text into the Word document (potentially with layout information)
            new_page.insert_textbox({
                "text": text,
                "fontsize": 12,  # Adjust as needed
                "rect": [10, 10, page.media_box.width - 20, page.media_box.height - 20]  # Adjust margins as needed
            })

        word_doc.save(output_path)
        print(f"PDF converted to Word with OCR: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
pdf_to_word_ocr("your_pdf.pdf", "output.docx")
