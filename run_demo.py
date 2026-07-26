from ingestion.ingest import run_ingestion
from app.answer_engine import generate_answer

if __name__ == "__main__":
    run_ingestion()

    question = input("Ask a question about your enterprise PDFs: ")

    result = generate_answer(question)

    print("\nAnswer")
    print("------")
    print(result["answer"])
    print("\nExported report:")
    print(result["export_path"])