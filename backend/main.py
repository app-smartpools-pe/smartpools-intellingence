from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# Permitir CORS para todas las rutas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clase para el cuerpo del request
class Message(BaseModel):
    message: str

# Crear cliente de OpenAI con clave desde variable de entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat(request: Message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Puedes cambiarlo a "gpt-3.5-turbo" si deseas
            messages=[
                {"role": "system", "content": "Eres un asistente de atención para una empresa de piscinas llamada SmartPools.pe"},
                {"role": "user", "content": request.message}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
