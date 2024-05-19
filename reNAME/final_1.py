import os
import re
import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
    return text

def parse_text(text):
    name_pattern = re.compile(r"Name\s*–\s*(.+)")
    limit1_pattern = re.compile(r"Limit 1\s*-\s*\$([\d,]+)")
    limit2_pattern = re.compile(r"Limit 2\s*-\s*\$([\d,]+)")
    company_pattern = re.compile(r"Company\s*–\s*(.+)")
    underwriting_company_pattern = re.compile(r"Underwriting Company\s*–\s*(.+)")

    name = name_pattern.search(text).group(1).strip()
    limit1 = limit1_pattern.search(text).group(1).replace(',', '').strip()
    limit2 = limit2_pattern.search(text).group(1).replace(',', '').strip()
    company = company_pattern.search(text).group(1).strip()
    underwriting_company = underwriting_company_pattern.search(text).group(1).strip()

    return name, limit1, limit2, company, underwriting_company

def generate_new_filename(name, limit1, limit2, company, underwriting_company):
    company_code = "SAF" if "Safeco" in company else ""
    underwriting_company_code = "TRA" if "Travelers" in underwriting_company else ""
    
    new_filename = f"{name} ${limit1} ${limit2} {company_code} {underwriting_company_code}.pdf"
    return new_filename

def rename_file(old_path, new_filename):
    new_path = os.path.join(os.path.dirname(old_path), new_filename)
    os.rename(old_path, new_path)
    return new_path

def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    name, limit1, limit2, company, underwriting_company = parse_text(text)
    new_filename = generate_new_filename(name, limit1, limit2, company, underwriting_company)
    new_path = rename_file(pdf_path, new_filename)
    print(f"File renamed to: {new_path}")

# Example usage:
pdf_path = r'C:\Users\AdminT\Desktop\Sample.pdf'
main(pdf_path)
