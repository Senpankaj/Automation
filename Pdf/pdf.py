import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
      reader = PyPDF2.PdfFileReader(file)
      text = ""
      for page in reader.pages:
            text += page.extract_text()
    return text

pdf_text = read_pdf(r"Desktop\Sample.pdf")

print(pdf_text)


                 
