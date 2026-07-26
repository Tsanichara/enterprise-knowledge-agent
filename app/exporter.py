import os
from datetime import datetime

def export_answer_markdown(result):
    os.makedirs("data/outputs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"data/outputs/knowledge_answer_{timestamp}.md"

    with open(path, "w", encoding="utf-8") as file:
        file.write("# Enterprise Knowledge Agent Report\n\n")
        file.write(f"## Question\n\n{result['query']}\n\n")
        file.write("## Answer\n\n")
        file.write(result["answer"])
        file.write("\n\n## Citations\n\n")

        for citation in result["citations"]:
            file.write(f"- {citation['label']}\n")

    return path

