from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()
HUGGINGFACE_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: UserMessage):
    payload = {"inputs": msg.message}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    generated_text = response.json()[0]["generated_text"]
    return {"response": generated_text}