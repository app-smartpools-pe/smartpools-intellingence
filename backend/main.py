from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.chatbot import generar_respuesta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    mensaje = data.get("mensaje", "")
    respuesta = generar_respuesta(mensaje)
    return {"respuesta": respuesta}