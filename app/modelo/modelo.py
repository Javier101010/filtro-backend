from ollama import chat
import json

def llamar_modelo(resultado):

    prompt = f"""
    Eres un profesor de procesamiento digital de imágenes.

    Explica el siguiente resultado:

    {resultado}

    Responde únicamente JSON válido con este formato:


    """

    respuesta = chat(
        model="qwen2.5vl",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    contenido = respuesta["message"]["content"]

    return json.loads(contenido)