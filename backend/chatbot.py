from transformers import pipeline

# Cargamos un modelo multilingüe de Hugging Face
pipe = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

def generar_respuesta(mensaje):
    respuesta = pipe(mensaje)[0]["generated_text"]
    return respuesta.strip()
