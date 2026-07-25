from retrieval.dense_retriever import dense_search
from retrieval.sparse_retriever import sparse_search

def hybrid_search(query: str, top_k: int = 8):
    dense_results = dense_search(query, top_k)
    sparse_results = sparse_search(query, top_k)

    merged = {}

    for result in dense_results + sparse_results:
        doc_id = result['id']

        if doc_id not in merged:
            merged[doc_id] = result
            merged[doc_id]["sources_found_by"] = [result["retrieval_type"]]
        else:
            merged[doc_id]["sources_found_by"].append(result["retrieval_type"])
        
        final_results = list(merged.values())

        final_results.sort(
            key=lambda item: len(item["sources_found_by"]), reverse=True
        )

    return final_results[:top_k]

