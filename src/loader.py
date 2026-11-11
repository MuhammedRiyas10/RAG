
from pypdf import PdfReader
import os

def load_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def load_documents(folder_path):

    documents = []

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            file_path = os.path.join(folder_path, file)

            text = load_pdf(file_path)

            documents.append({
                "filename": file,
                "content": text
            })

    return documents
