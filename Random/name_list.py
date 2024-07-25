import fitz  # PyMuPDF

# Open the PDF file
pdf_path = "C:\\Users\\Pankaj's PC\\Downloads\\list.pdf"
document = fitz.open(pdf_path)

# Initialize a list to store the insurance company names
insurance_companies = []

# Iterate over each page
for page_num in range(document.page_count):
    page = document.load_page(page_num)
    text = page.get_text("text")
    lines = text.split('\n')
    
    # Identify patterns for company names based on lines of text
    for line in lines:
        if line.strip().isupper() and ("COMPANY" in line or "CORPORATION" in line or "INC" in line):
            insurance_companies.append(line.strip())

# Print the list of insurance companies
print(insurance_companies)
