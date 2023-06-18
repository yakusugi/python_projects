import PyPDF2
import docx

# Step 3: Open the Word file
doc = docx.Document('sample.docx')

# Step 4: Create a PDF object
pdf_file = PyPDF2.PdfWriter()

# Step 5: Iterate through each page of the Word file
for para in doc.paragraphs:
    pdf_file.add_page(para.text)

# Step 6: Create the PDF file
with open('example.pdf', 'wb') as f:
    pdf_file.write(f)

print("File converted successfully!")


