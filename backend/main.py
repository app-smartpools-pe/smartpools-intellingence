
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en piscinas para una empresa peruana llamada SmartPools."},
            {"role": "user", "content": user_message}
        ]
    )
    return {"reply": response.choices[0].message["content"]}
