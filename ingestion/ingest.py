from ingestion.pdf_loader import load_pdfs
from ingestion.chunker import chunk_documents
from retrieval.sparse_retriever import index_sparse_documents
from retrieval.dense_retriever import index_dense_documents
from graph.graph_store import build_graph_from_chunks, graph_stats

PDF_FOLDER = "data/pdfs"

GLOBAL_CHUNKS = []

def run_ingestion():
    global GLOBAL_CHUNKS

    print("Loading PDFs...")
    documents = load_pdfs(PDF_FOLDER)

    print("Chunking documents...")
    chunks = chunk_documents(documents)
    GLOBAL_CHUNKS = chunks

    print("Indexing dense retrieval...")
    index_dense_documents(chunks)

    print("Indexing sparse retrieval...")
    index_sparse_documents(chunks)

    print("Building knowledge graph...")
    build_graph_from_chunks(chunks)

    print("Ingestion complete.")
    print("Documents:", len(documents))
    print("Chunks:", len(chunks))
    print("Graph:", graph_stats())

    return chunks


if __name__ == "__main__":
    run_ingestion()

