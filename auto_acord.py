from transformers import pipeline
from PyPDF2 import PdfFileWriter, PdfFileReader
import requests

# Step 1: Extract Information from Text
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def extract_information(text):
    ner_results = ner_pipeline(text)
    extracted_info = {}

    for entity in ner_results:
        entity_type = entity['entity'].split('-')[-1]
        if entity_type not in extracted_info:
            extracted_info[entity_type] = []
        extracted_info[entity_type].append(entity['word'])

    return extracted_info

# Step 2: Fill an ACORD Form
def fill_acord_form(template_path, output_path, info):
    template_pdf = PdfFileReader(template_path)
    output_pdf = PdfFileWriter()

    # Copy the template PDF to the output
    for i in range(template_pdf.getNumPages()):
        output_pdf.addPage(template_pdf.getPage(i))

    # Add extracted information to the form fields
    form_fields = output_pdf.getFields()
    for field in form_fields:
        if field in info:
            form_fields[field] = info[field]

    with open(output_path, 'wb') as f:
        output_pdf.write(f)

# Step 3: Fetch Information from CRM
def fetch_info_from_crm(crm_api_url, insured_id):
    response = requests.get(f"{crm_api_url}/api/insured/{insured_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from CRM")

# Example Usage
sample_text = """
John Doe lives at 123 Main St, Springfield, and his email is john.doe@example.com.
He drives a 2019 Tesla Model 3 with VIN 5YJ3E1EA7JF000000.
"""
info = extract_information(sample_text)
template_path = 'ACORD_Template.pdf'
output_path = 'Filled_ACORD_Form.pdf'

# Fill the form with the extracted information
fill_acord_form(template_path, output_path, info)

# Fetch additional information from CRM and update the form
crm_api_url = 'https://example-crm.com'
insured_id = '12345'
crm_info = fetch_info_from_crm(crm_api_url, insured_id)
info.update(crm_info)

# Fill the form again with the additional information
fill_acord_form(template_path, output_path, info)