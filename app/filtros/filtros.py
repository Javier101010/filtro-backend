import numpy as np

def preparar_imagen(imagen: np.ndarray, k: int = 3):
    offset = k // 2

    img = np.array(imagen)

    img_padded = np.pad(
        img,
        pad_width=offset,
        mode='edge'
    )

    return img, img_padded, offset


def filtro_media(imagen: np.ndarray):
    img, img_padded, offset = preparar_imagen(imagen)

    mascara = np.ones((3, 3)) / 9

    resultado = np.zeros_like(img, dtype=float)

    for i in range(offset, img_padded.shape[0] - offset):
        for j in range(offset, img_padded.shape[1] - offset):

            ventana = img_padded[
                i-offset:i+offset+1,
                j-offset:j+offset+1
            ]

            valor = np.sum(ventana * mascara)

            resultado[i-offset, j-offset] = valor

    resultado = resultado.astype(np.uint8)

    return resultado


def filtro_mediana(imagen: np.ndarray):
    img, img_padded, offset = preparar_imagen(imagen)

    resultado = np.zeros_like(img, dtype=float)

    for i in range(offset, img_padded.shape[0] - offset):
        for j in range(offset, img_padded.shape[1] - offset):

            ventana = img_padded[
                i-offset:i+offset+1,
                j-offset:j+offset+1
            ]

            resultado[i-offset, j-offset] = np.median(ventana)

    resultado = resultado.astype(np.uint8)

    return resultado


def normalizar(resultado):
    min_val = np.min(resultado)
    max_val = np.max(resultado)

    m = 255 / (max_val - min_val)
    b = -m * min_val

    resultado = m * resultado + b

    return resultado.astype(np.uint8)


def filtro_sobel(imagen: np.ndarray):
    img, img_padded, offset = preparar_imagen(imagen)

    mascara = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

    resultado = np.zeros_like(img, dtype=float)

    for i in range(offset, img_padded.shape[0] - offset):
        for j in range(offset, img_padded.shape[1] - offset):

            ventana = img_padded[
                i-offset:i+offset+1,
                j-offset:j+offset+1
            ]

            resultado[i-offset, j-offset] = np.sum(ventana * mascara)

    resultado = normalizar(resultado)

    return resultado


def filtro_laplaciano(imagen: np.ndarray):
    img, img_padded, offset = preparar_imagen(imagen)

    mascara = np.array([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ])

    resultado = np.zeros_like(img, dtype=float)

    for i in range(offset, img_padded.shape[0] - offset):
        for j in range(offset, img_padded.shape[1] - offset):

            ventana = img_padded[
                i-offset:i+offset+1,
                j-offset:j+offset+1
            ]

            resultado[i-offset, j-offset] = np.sum(ventana * mascara)

    resultado = normalizar(resultado)

    return resultado