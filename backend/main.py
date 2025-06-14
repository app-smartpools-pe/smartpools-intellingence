from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: UserMessage):
    response = chatbot(msg.message, max_length=100, do_sample=False)[0]["generated_text"]
    return {"response": response}