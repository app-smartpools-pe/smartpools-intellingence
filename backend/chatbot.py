from transformers import pipeline

# Cargar modelo Falcon RW 1B desde Hugging Face
pipe = pipeline(
    "text-generation",
    model="tiiuae/falcon-rw-1b",
    trust_remote_code=True,
    max_new_tokens=200,
    do_sample=True,
    temperature=0.7,
)

def generar_respuesta(mensaje):
    # Prompt con contexto para guiar al modelo
    prompt = (
        "Eres un asistente virtual experto en piscinas, trabajando para la empresa smartpools Perú.\n"
        "Brindas información clara, profesional y amable sobre servicios como:\n"
        "- Diseño y construcción de piscinas\n"
        "- Mantenimiento preventivo y correctivo\n"
        "- Instalación de bombas, filtros y calentadores\n"
        "- Automatización de sistemas de piscinas\n"
        "- Limpieza y tratamiento de agua\n\n"
        f"Cliente: {mensaje}\n"
        "Asistente:"
    )

    try:
        resultado = pipe(prompt)[0]["generated_text"]
        # Recorta la respuesta a partir de "Asistente:"
        if "Asistente:" in resultado:
            respuesta = resultado.split("Asistente:")[1].strip()
        else:
            respuesta = resultado.strip()
        return respuesta
    except Exception as e:
        return f"Ocurrió un error al generar la respuesta: {str(e)}"
