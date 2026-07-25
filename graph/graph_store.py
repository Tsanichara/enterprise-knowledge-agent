import networkx as nx
from graph.entity_extractor import extract_entities

GRAPH = nx.Graph()

def build_graph_from_chunks(chunks):
    for chunk in chunks:
        entities = extract_entities(chunk["text"])

        for entity in entities:
            GRAPH.add_node(entity, type='entity')

        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):
                GRAPH.add_edge(
                    entities[i],
                    entities[j],
                    source=chunk['source'],
                    page=chunk['page'],
                    relationship='co_occurs_with'
                )

    return GRAPH

def get_related_entities(entity: str, max_neighbors: int = 5):
    if entity not in GRAPH:
        return []

    neighbors = list(GRAPH.neighbors(entity))[:max_neighbors]
    return neighbors

def graph_stats():
    return {
        "nodes": GRAPH.number_of_nodes(),
        "edges": GRAPH.number_of_edges()
    }
