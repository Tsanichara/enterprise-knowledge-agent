from fastapi import FastAPI
from pydantic import BaseModel

from ingestion.ingest import run_ingestion
from app.answer_engine import generate_answer

app = FastAPI(title="Enterprise Knowledge Agent")

class QueryRequest(BaseModel):
    query: str

@app.on_event("startup")
def startup_event():
    run_ingestion()

@app.get("/")
def home():
    return {"message": "Enterprise Knowledge Agent is running."}

@app.post("/ask")
def ask_question(request: QueryRequest):
    result = generate_answer(request.question)
    return result
