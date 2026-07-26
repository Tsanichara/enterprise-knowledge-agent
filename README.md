# Enterprise Knowledge Agent

Local RAG system for enterprise PDFs with hybrid retrieval, graph enrichment, citations, and markdown report export.

## Features

- PDF ingestion from `data/pdfs`
- Text chunking with overlap
- Hybrid retrieval (dense: Chroma + sentence-transformers; sparse: TF-IDF + cosine similarity)
- Knowledge graph entity enrichment
- Citation generation
- CLI and FastAPI interfaces

## Setup

Requirements:

- Python 3.10+
- pip

Install:

```bash
pip install -r requirements.txt
```

## Usage

1. Add PDF files to `data/pdfs`.
2. Run one of the following:

CLI:

```bash
python run_demo.py
```

API:

```bash
uvicorn app.main:app --reload
```

Example API request:

```bash
curl -X POST "http://127.0.0.1:8000/ask" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"query":"What does our documentation say about AI Governance, risk controls, and monitoring?"}'
```

## Endpoints

- `GET /` returns service status
- `POST /ask` accepts:

```json
{
  "query": "your question"
}
```

## Output

- Answers include retrieved context, graph context, and citations
- Markdown reports are exported to `data/outputs`

## Project Layout

```text
app/           API and answer assembly
citations/     citation formatting
graph/         entity extraction and graph enrichment
ingestion/     PDF loading, chunking, and indexing pipeline
retrieval/     dense, sparse, and hybrid retrieval
data/pdfs/     input documents
data/outputs/  generated reports
```

## Note

The API runs ingestion on startup. If you re-ingest with the same IDs and need a clean rebuild, clear `data/chroma_db` first.
