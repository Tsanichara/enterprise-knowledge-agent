def build_citations(retrieved_chunks):
    citations = []

    seen = set()
    citation_index = 1

    for chunk in retrieved_chunks:
        key = f"{chunk['source']}-p{chunk['page']}"

        if key in seen:
            continue

        seen.add(key)

        citations.append({
            "citation_id": citation_index,
            "source": chunk["source"],
            "page": chunk["page"],
            "label": f'[{citation_index}] {chunk["source"]}, page {chunk["page"]}'
        })
        citation_index += 1

    return citations


def format_context_with_citations(retrieved_chunks):
    lines = []

    for index, chunk in enumerate(retrieved_chunks, start=1):
        lines.append(f"""
[Citation {index}]
Source: {chunk['source']}
Page: {chunk['page']}
Text:
{chunk['text']}
""")

    return "".join(lines)
    

