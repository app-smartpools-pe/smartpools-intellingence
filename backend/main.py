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

    try:
        data = response.json()
        # Si la respuesta es una lista con al menos un resultado válido
        if isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
            generated_text = data[0]["generated_text"]
        else:
            generated_text = "La IA no generó respuesta. Revisa si el modelo está activo o disponible."
    except Exception as e:
        print("ERROR procesando la respuesta:", e)
        print("Contenido recibido:", response.text)
        generated_text = "Ocurrió un error al procesar la respuesta de la IA."

    return {"response": generated_text}
