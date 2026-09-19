from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


CARPETA = Path(__file__).resolve().parent
ENTRADA_SOLICITADA = CARPETA / "image.png"
ENTRADA_ALTERNATIVA = CARPETA / "Imagen2.jpg"
SALIDA = CARPETA / "resultados"
SALIDA.mkdir(exist_ok=True)

# Localizar la imagen solicitada y preparar la carpeta de resultados.
entrada = ENTRADA_SOLICITADA if ENTRADA_SOLICITADA.exists() else ENTRADA_ALTERNATIVA
if not entrada.exists():
    raise FileNotFoundError("No se encontró image.png ni Imagen2.jpg")

# Cargar la imagen con PIL y convertirla en un arreglo NumPy RGB.
imagen = Image.open(entrada)
imagen_np = np.array(imagen.convert("RGB"))
alto, ancho, canales = imagen_np.shape

# Función para guardar cada imagen resultante como archivo PNG.
def guardar_figura(nombre, imagen_mostrada, titulo=None, cmap=None):
    plt.figure(figsize=(8, 5))
    plt.imshow(imagen_mostrada, cmap=cmap)
    if titulo:
        plt.title(titulo)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(SALIDA / nombre, dpi=150, bbox_inches="tight")
    plt.close()


# Función para obtener el valor RGB de un píxel específico.
def pixel_en(fila, columna):
    if fila >= alto or columna >= ancho:
        return "fuera de los límites"
    return imagen_np[fila, columna].tolist()


# Mostrar y guardar la imagen original.
guardar_figura("01_original.png", imagen_np, "Imagen original")

# Separar los tres canales RGB y mostrar cada canal.
rojo = imagen_np[:, :, 0]
verde = imagen_np[:, :, 1]
azul = imagen_np[:, :, 2]
canales_rgb = {"rojo": rojo, "verde": verde, "azul": azul}

for nombre, canal in canales_rgb.items():
    guardar_figura(f"canal_{nombre}.png", canal, f"Canal {nombre}", cmap="gray")

# Convertir la imagen a escala de grises y mostrarla.
imagen_gris = imagen.convert("L")
gris_np = np.array(imagen_gris)
guardar_figura("02_escala_grises.png", gris_np, "Escala de grises", cmap="gray")

# Crear una copia y pintar de rojo un cuadro de 100 x 100 píxeles.
imagen_modificada = imagen_np.copy()
imagen_modificada[: min(100, alto), : min(100, ancho)] = [255, 0, 0]
guardar_figura("03_cuadro_rojo.png", imagen_modificada, "Cuadro rojo de 100 x 100 píxeles")

# Crear copias eliminando individualmente los canales rojo, verde y azul.
sin_rojo = imagen_np.copy()
sin_rojo[:, :, 0] = 0
sin_verde = imagen_np.copy()
sin_verde[:, :, 1] = 0
sin_azul = imagen_np.copy()
sin_azul[:, :, 2] = 0

sin_canales = {
    "sin_rojo": sin_rojo,
    "sin_verde": sin_verde,
    "sin_azul": sin_azul,
}
for nombre, imagen_sin_canal in sin_canales.items():
    guardar_figura(f"{nombre}.png", imagen_sin_canal, nombre.replace("_", " ").title())

# Crear imágenes binarias usando los umbrales solicitados.
binarias = {}
for umbral in (80, 128, 180):
    binaria = np.where(gris_np < umbral, 0, 255).astype(np.uint8)
    binarias[umbral] = binaria
    guardar_figura(f"binaria_{umbral}.png", binaria, f"Imagen binaria, umbral {umbral}", cmap="gray")

# Calcular promedios, mínimos y máximos de cada canal RGB.
promedios = {nombre: float(np.mean(canal)) for nombre, canal in canales_rgb.items()}
minimos = {nombre: int(np.min(canal)) for nombre, canal in canales_rgb.items()}
maximos = {nombre: int(np.max(canal)) for nombre, canal in canales_rgb.items()}

# Calcular estadísticas y clasificación de píxeles en escala de grises.
promedio_gris = float(np.mean(gris_np))
minimo_gris = int(np.min(gris_np))
maximo_gris = int(np.max(gris_np))
conteos_gris = {
    "oscuros": int(np.sum(gris_np < 85)),
    "medios": int(np.sum((gris_np >= 85) & (gris_np <= 170))),
    "claros": int(np.sum(gris_np > 170)),
}

# Obtener las matrices pequeñas solicitadas y el píxel central.
matriz_5x5 = imagen_np[:5, :5]
matriz_gris_10x10 = gris_np[:10, :10]
centro = pixel_en(alto // 2, ancho // 2)

# Mostrar dimensiones, valores RGB y la matriz de los primeros 5 x 5 píxeles.
print("Imagen utilizada:", entrada.name)
print("Dimensiones RGB:", imagen_np.shape)
print("Alto:", alto, "Ancho:", ancho, "Canales:", canales)
print("Pixel (0, 0):", pixel_en(0, 0))
print("Pixel (10, 10):", pixel_en(10, 10))
print("Pixel (50, 50):", pixel_en(50, 50))
print(f"Pixel central ({alto // 2}, {ancho // 2}):", centro)
print("Matriz RGB 5x5:\n", matriz_5x5)

# Mostrar las dimensiones y estadísticas de cada canal RGB.
for nombre, canal in canales_rgb.items():
    print(f"Canal {nombre}: dimensiones={canal.shape}, promedio={promedios[nombre]:.2f}, "
          f"mínimo={minimos[nombre]}, máximo={maximos[nombre]}")
print("Canal con mayor promedio:", max(promedios, key=promedios.get))

# Mostrar la matriz de grises, sus estadísticas y los conteos solicitados.
print("Dimensiones escala de grises:", gris_np.shape)
print("Matriz de grises 10x10:\n", matriz_gris_10x10)
print("Promedio de grises:", promedio_gris)
print("Mínimo de grises:", minimo_gris)
print("Máximo de grises:", maximo_gris)
print("Conteo de grises:", conteos_gris)
print("Imágenes guardadas en:", SALIDA)