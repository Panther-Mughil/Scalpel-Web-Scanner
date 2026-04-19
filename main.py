from fastapi import FastAPI
from pydantic import BaseModel
from scanner import run_scan

app = FastAPI()

class ScanRequest(BaseModel):
    target: str

@app.get("/")
def home():
    return {"message": "Scanner is Alive!"}

@app.post("/scan")
def scan(request: ScanRequest):
    result = run_scan(request.target)
    return result