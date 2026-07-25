from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DOCUMENTS = []
VECTORIZER = None
TFIDF_MATRIX = None

def index_sparse_documents(chunks):
    global DOCUMENTS, VECTORIZER, TFIDF_MATRIX

    DOCUMENTS = chunks
    texts = [chunk["text"] for chunk in chunks]

    VECTORIZER = TfidfVectorizer(stop_words='english')
    TFIDF_MATRIX = VECTORIZER.fit_transform(texts)

def sparse_search(query: str, top_k: int = 5):
    if VECTORIZER is None or TFIDF_MATRIX is None:
        return []
    
    query_vector = VECTORIZER.transform([query])
    similarities = cosine_similarity(query_vector, TFIDF_MATRIX).flatten()

    ranked_indices = similarities.argsort()[::-1][:top_k]

    results = []

    for index in ranked_indices:
        chunk = DOCUMENTS[index]
        results.append({
            'id': chunk['id'],
            'text': chunk['text'],
            'source': chunk['source'],
            'page': chunk['page'],
            'score': float(similarities[index]),
            'retrieval_type': 'sparse'
        })

    return results

