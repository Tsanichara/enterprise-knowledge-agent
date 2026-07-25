def chunk_text(text: str, chunk_size: int = 700, overlap: int = 120):
    words = text.split()
    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = ' '.join(words[start:end])
        chunks.append(chunk)

        start += chunk_size - overlap  # Move the start index forward with overlap

    return chunks

def chunk_documents(documents):
    chunked_documents = []
    chunk_id = 0

    for doc in documents:
        chunks = chunk_text(doc['text'])

        for chunk in chunks:
            chunked_documents.append({
                'id': f"chunk-{chunk_id}",
                'source': doc['source'],
                'page': doc['page'],
                'text': chunk
            })
            chunk_id += 1
        
    return chunked_documents

