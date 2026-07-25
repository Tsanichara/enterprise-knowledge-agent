import chromadb
from sentence_transformers import SentenceTransformer

DB_PATH = "data/chroma_db"
COLLECTION_NAME = "enterprise_docs"

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_collection():
    client = chromadb.PersistentClient(path=DB_PATH)
    return client.get_or_create_collection(COLLECTION_NAME)

def index_dense_documents(chunks):
    collection = get_collection()

    for chunk in chunks:
        embedding = embedding_model.encode(chunk["text"]).tolist()

        collection.add(
            ids=[chunk["id"]],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[{
                'source': chunk['source'],
                'page': chunk['page']
            }]
        )

def dense_search(query: str, top_k: int = 5):
    collection = get_collection()
    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    matches = []

    for doc, meta_data, doc_id in zip(results['documents'][0], results['metadatas'][0], results['ids'][0]):
        matches.append({
            'id': doc_id,
            'text': doc,
            'source': meta_data['source'],
            'page': meta_data['page'],
            "retrieval_type": 'dense'
        })

    return matches