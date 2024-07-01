from tika import parser

# Extract text from a PDF file
raw = parser.from_file("C:\\Users\\AdminT\\Documents\\Research Papers\\mach.pdf")
text = raw['content']

# Print the extracted text
print(text)