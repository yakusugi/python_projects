from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Open the Word file
doc = Document('sample.docx')

# Create a PDF object
pdf_file = SimpleDocTemplate("example.pdf", pagesize=letter)

# Create a list to hold the text from the Word document
text = []

# Iterate through each paragraph in the Word document
for para in doc.paragraphs:
    text.append(para.text)

# Add the text to the PDF document
pdf_file.build(text)

print("File converted successfully!")



