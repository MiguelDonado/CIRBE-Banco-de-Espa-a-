import os
import pdfplumber


def get_pdf_files():
    # It'll return the name of the PDF file in the folder. If there´s more or less than one PDF file, it'll raise an error
    pdf_files = [f for f in os.listdir(".") if f.endswith(".pdf")]
    if len(pdf_files) != 1:
        raise ValueError("It's to be just one PDF file in the folder")
    return pdf_files[0]


def extract_data_from_pdf(pdf_file):
    # It'll return the text from the PDF file as one string
    with pdfplumber.open(pdf_file) as pdf:
        text_file = [page.extract_text() for page in pdf.pages]
    return "\n".join(text_file)
