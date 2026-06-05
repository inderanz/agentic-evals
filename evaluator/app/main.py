from fastapi import FastAPI
from pydantic import BaseModel
from evaluator import evaluate_repo

app = FastAPI(title="Enterprise AI Capability Evaluator")

class EvalRequest(BaseModel):
    repo_url: str
    sha: str

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/api/v1/evaluate")
def evaluate(req: EvalRequest):
    return evaluate_repo(req.repo_url, req.sha)
