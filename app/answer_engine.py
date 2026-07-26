from retrieval.hybrid_retriever import hybrid_search
from graph.graph_enrichment import enrich_with_graph_context
from citations.citation_builder import build_citations, format_context_with_citations
from app.exporter import export_answer_markdown

def generate_answer(query: str):
    retrieved_chunks = hybrid_search(query)
    graph_context = enrich_with_graph_context(query, retrieved_chunks)
    citations = build_citations(retrieved_chunks)
    formatted_context = format_context_with_citations(retrieved_chunks)

    answer = f"""
Enterprise Knowledge Agent Answer

Question:
{query}

Answer:
Based on the retrieved enterprise documents, the system found relevant information across the cited sources.

Key Findings:
"""

    for chunk in retrieved_chunks[:4]:
        answer += f"""
- {chunk["text"][:350]}...
  Source: {chunk["source"]}, page {chunk["page"]}
"""

    answer += """
Knowledge Graph Enrichment:
"""

    for item in graph_context:
        answer += f"""
- {item["entity"]} is related to: {", ".join(item["related_entities"])}
"""

    answer += """
Citations:
"""

    for citation in citations:
        answer += f"""
{citation["label"]}
"""

    if formatted_context.strip():
        answer += f"""

Retrieved Context:
{formatted_context}
"""

    result = {
        "query": query,
        "answer": answer,
        "retrieved_chunks": retrieved_chunks,
        "graph_context": graph_context,
        "citations": citations,
        "formatted_context": formatted_context
    }

    result["export_path"] = export_answer_markdown(result)

    return result


    