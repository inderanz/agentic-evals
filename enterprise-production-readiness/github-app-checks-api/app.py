from fastapi import FastAPI, Header, HTTPException, Request
import hmac
import hashlib
import os

app = FastAPI(title="AI Capability GitHub App Webhook")

WEBHOOK_SECRET = os.environ.get("GITHUB_WEBHOOK_SECRET", "")

def verify_signature(raw_body: bytes, signature: str | None) -> None:
    if not WEBHOOK_SECRET:
        raise HTTPException(status_code=500, detail="Webhook secret not configured")
    if not signature:
        raise HTTPException(status_code=401, detail="Missing GitHub signature")
    expected = "sha256=" + hmac.new(WEBHOOK_SECRET.encode(), raw_body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        raise HTTPException(status_code=401, detail="Invalid GitHub signature")

@app.post("/github/webhook")
async def github_webhook(request: Request, x_hub_signature_256: str | None = Header(default=None)):
    raw = await request.body()
    verify_signature(raw, x_hub_signature_256)
    event = await request.json()
    # enqueue evaluation job using repo, sha, installation id
    return {"accepted": True}
