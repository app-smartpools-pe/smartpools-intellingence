from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()
HUGGINGFACE_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom-560m"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: UserMessage):
    payload = {"inputs": msg.message}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    try:
        data = response.json()
        print("Respuesta Hugging Face:", data)  # Esto imprimirá en los logs del servidor

        if isinstance(data, list) and "generated_text" in data[0]:
            return {"response": data[0]["generated_text"]}
        elif "error" in data:
            return {"response": f"Error del modelo: {data['error']}"}
        else:
            return {"response": "La IA no generó respuesta. Revisa si el modelo está activo o disponible."}
    except Exception as e:
        print("Error al procesar respuesta:", str(e))
        return {"response": "Ocurrió un error al procesar la respuesta de la IA."}
