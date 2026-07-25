import re

STOPWORDS = {
    "The", "This", "That", "These", "Those", "And", "But",
    "For", "With", "From", "When", "Where", "Which"
}

def extract_entities(text: str):
    candidates = re.findall(r"\b[A-Z][A-Za-z0-9\-]*(?:\s+[A-Z][A-Za-z0-9\-]*)*\b", text)

    entities = []

    for candidate in candidates:
        cleaned = candidate.strip()

        if cleaned not in STOPWORDS and len(cleaned) > 2:
            entities.append(cleaned)

    return list(set(entities))