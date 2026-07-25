from graph.entity_extractor import extract_entities
from graph.graph_store import get_related_entities

def enrich_with_graph_context(query: str, retrieved_chunks):
    query_entities = extract_entities(query)

    chunk_entities = []

    for chunk in retrieved_chunks:
        chunk_entities.extend(extract_entities(chunk["text"]))

    all_entities = list(set(query_entities + chunk_entities))

    enriched_context = []

    for entity in all_entities[:10]:
        related = get_related_entities(entity)

        if related:
            enriched_context.append({
                "entity": entity,
                "related_entities": related
            })

    return enriched_context

