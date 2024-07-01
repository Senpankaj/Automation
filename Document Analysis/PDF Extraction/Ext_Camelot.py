import camelot
import os

def extract_tables_from_pdf(pdf_path, output_md_path):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)

    # Extract tables from PDF
    tables = camelot.read_pdf(pdf_path, pages='all')

    # Open the markdown file in write mode
    with open(output_md_path, 'w') as md_file:
        md_file.write("# Extracted Tables\n\n")

        for i, table in enumerate(tables):
            md_file.write(f"## Table {i+1}\n")
            md_file.write("```\n")
            md_file.write(table.df.to_markdown(index=False))
            md_file.write("\n```\n\n")

            # Example of highlighting a section
            md_file.write(f"### Highlighted Section for Table {i+1}\n")
            md_file.write("This section is highlighted to specify important details.\n\n")

if __name__ == "__main__":
    pdf_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\12.pdf"
    output_md_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\mach.md"
    extract_tables_from_pdf(pdf_path, output_md_path)

