from PyPDF2 import PdfReader
import os
import string
import re

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_info(text):
    # Adjust the regex based on the actual text format in your PDF
    name_pattern = r"Name – ([A-Za-z ]+)"  # Match name after "Name – "
    date_pattern = r"Date – (\d{2}/\d{2}/\d{4})"  # Match date after "Date – "
    limit_pattern = r"Limit 1 - \$([\d,]+)"  # Match limit after "Limit 1 - $"

    name_match = re.search(name_pattern, text)
    date_match = re.search(date_pattern, text)
    limit_match = re.search(limit_pattern, text)

    name = name_match.group(1).strip() if name_match else "UnknownName"
    date = date_match.group(1).strip() if date_match else "UnknownDate"
    limit = limit_match.group(1).strip() if limit_match else "UnknownLimit"

    # Convert date from dd/mm/yyyy to MM/DD/YYYY
    if date != "UnknownDate":
        day, month, year = date.split('/')
        date = f"{month}/{day}/{year}"

    return name, date, limit

def sanitize_filename(filename):
    valid_chars = "-_.() /%s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)

def rename_pdf(file_path):
    text = read_pdf(file_path)
    name, date, limit = extract_info(text)
    new_file_name = f"{name}_{date}_{limit}.pdf"
    
    new_file_name = sanitize_filename(new_file_name)

    new_path = os.path.join(os.path.dirname(file_path), new_file_name)
    os.rename(file_path, new_path)
    print(f"File renamed to: {new_file_name}")

# Test the function
rename_pdf('Sample.pdf')
