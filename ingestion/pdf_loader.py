import os
import fitz

def load_pdfs(pdf_folder: str):
    documents = []

    for filename in os.listdir(pdf_folder):
        if not filename.lower().endswith('.pdf'):
            continue

        path = os.path.join(pdf_folder, filename)
        doc = fitz.open(path)

        for page_number, page in enumerate(doc, start=1):
            text = page.get_text()

            if text.strip():  # Only add non-empty pages
                documents.append({
                    'source': filename,
                    'page': page_number,
                    'text': text
                })
                
    return documents