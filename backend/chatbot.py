from transformers import pipeline

# Cargamos un modelo multilingüe de Hugging Face
modelo = pipeline("text-generation", model="tiiuae/falcon-rw-1b", max_new_tokens=100)

def generar_respuesta(mensaje):
    respuesta = modelo(mensaje)[0]["generated_text"]
    return respuesta.strip()