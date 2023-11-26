import os
import pandas as pd
from PyPDF2 import PdfFileReader

def parse_pdf_directory(directory):
    data = {'filename': [], 'text': []}
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            print(file_path)
            text = extract_text_from_pdf(file_path)
            data['filename'].append(filename)
            data['text'].append(text)
    return pd.DataFrame(data)

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        print('Scanning file - ',file_path)
        pdf_reader = PdfFileReader(file)
        text = ''
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
        return text