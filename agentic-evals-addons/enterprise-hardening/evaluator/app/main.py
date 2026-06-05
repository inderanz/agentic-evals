from fastapi import FastAPI
from pydantic import BaseModel
from evaluator import evaluate_local_repo

app = FastAPI(title="Enterprise Agentic Capability Evaluator")

class EvalRequest(BaseModel):
    repo_path: str = "."

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/api/v1/evaluate")
def evaluate(req: EvalRequest):
    return evaluate_local_repo(req.repo_path)
