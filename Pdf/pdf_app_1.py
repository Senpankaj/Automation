from flask import Flask, render_template, request
import PyPDF2
import os
import string
import re

app = Flask(__name__)

# Functions for file processing
def read_pdf(file):
    text = ""
    reader = PyPDF2.PdfFileReader(file)
    for page in range(reader.numPages):
        text += reader.getPage(page).extractText()
    return text

def extract_info(text):
    name_match = re.search(r"Name\s*-\s*([A-Za-z ]+)", text)
    date_match = re.search(r"Date\s*-\s*(\d{2}/\d{2}/\d{4})", text)
    limit_match = re.search(r"Limit 1\s*-\s*\$([\d,]+)", text)
    
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

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html', message='No selected file')
        
        if file:
            text = read_pdf(file)
            name, date, limit = extract_info(text)
            new_file_name = f"{name}_{date}_{limit}.pdf"
            new_file_name = sanitize_filename(new_file_name)
            new_path = os.path.join('uploads', new_file_name)
            file.save(new_path)
            return render_template('index.html', message=f'File uploaded and renamed to: {new_file_name}')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
