from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from PIL import Image
import io
import numpy as np

from app.filtros.filtros import (
    filtro_media,
    filtro_mediana,
    filtro_sobel,
    filtro_laplaciano,
    filtro_sobel_crudo,
    filtro_laplaciano_crudo
)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://filtro-imagenes-two.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def inicio():
    return {
        "mensaje": "Backend funcionando"
    }

def cargar_imagen(archivo: UploadFile):
    imagen = Image.open(archivo.file)

    imagen = imagen.convert("L")

    return np.array(imagen)

@app.post("/filtro/explicacion")
def obtener_explicacion(filtros: list[str], imagen: UploadFile = File(...)):
    matriz_original = cargar_imagen(imagen)
    media, mediana, sobel,sobel_crudo, laplaciano, laplaciano_crudo = None, None, None, None, None, None

    for filtro in filtros:
        if filtro == "media":
            media = filtro_media(matriz_original)
        elif filtro == "mediana":
            mediana = filtro_mediana(matriz_original)
        elif filtro == "sobel":
            sobel = filtro_sobel(matriz_original)
            sobel_crudo = filtro_sobel_crudo(matriz_original)
        elif filtro == "laplaciano":
            laplaciano = filtro_laplaciano(matriz_original)
            laplaciano_crudo = filtro_laplaciano_crudo(matriz_original)
    
    return {
        "matriz_original": matriz_original.tolist(),
        "filtro_media": media.tolist() if media is not None else None,
        "filtro_mediana": mediana.tolist() if mediana is not None else None,
        "filtro_sobel": sobel.tolist() if sobel is not None else None,
        "filtro_sobel_crudo": sobel_crudo.tolist() if sobel_crudo is not None else None,
        "filtro_laplaciano": laplaciano.tolist() if laplaciano is not None else None,
        "filtro_laplaciano_crudo": laplaciano_crudo.tolist() if laplaciano_crudo is not None else None
    }


@app.post("/filtro/media")
def aplicar_media(imagen: UploadFile = File(...)):
    img = cargar_imagen(imagen)

    resultado = filtro_media(img)

    resultado_pil = Image.fromarray(resultado)

    buffer = io.BytesIO()

    resultado_pil.save(
        buffer,
        format="JPEG"
    )

    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/jpeg"
    )


@app.post("/filtro/mediana")
def aplicar_mediana(imagen: UploadFile = File(...)):
    img = cargar_imagen(imagen)

    resultado = filtro_mediana(img)

    resultado_pil = Image.fromarray(resultado)

    buffer = io.BytesIO()

    resultado_pil.save(
        buffer,
        format="JPEG"
    )

    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/jpeg"
    )


@app.post("/filtro/sobel")
def aplicar_sobel(imagen: UploadFile = File(...)):
    img = cargar_imagen(imagen)

    resultado = filtro_sobel(img)

    resultado_pil = Image.fromarray(resultado)

    buffer = io.BytesIO()

    resultado_pil.save(
        buffer,
        format="JPEG"
    )

    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/jpeg"
    )


@app.post("/filtro/laplaciano")
def aplicar_laplaciano(imagen: UploadFile = File(...)):
    img = cargar_imagen(imagen)

    resultado = filtro_laplaciano(img)

    resultado_pil = Image.fromarray(resultado)

    buffer = io.BytesIO()

    resultado_pil.save(
        buffer,
        format="JPEG"
    )

    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="image/jpeg"
    )