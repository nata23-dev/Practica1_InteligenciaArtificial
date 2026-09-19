# Reporte de Imagen2.jpg

## Exploración

La imagen analizada es `Imagen2.jpg`.

- Dimensiones RGB: `(554, 554, 3)`
- Alto: `554` píxeles
- Ancho: `554` píxeles
- Canales: `3` (rojo, verde y azul)

En `imagen_np.shape`, la primera dimensión representa el alto, la segunda el ancho y la tercera los canales de color.

### Valores RGB

- Píxel `(0, 0)`: `[255, 255, 255]`
- Píxel `(10, 10)`: `[255, 255, 255]`
- Píxel `(50, 50)`: `[255, 255, 255]`
- Píxel central `(277, 277)`: `[171, 101, 65]`

Los primeros `5 x 5` píxeles son blancos, por lo que sus valores RGB son `[255, 255, 255]`.

## Canales RGB

Cada canal tiene dimensiones `(554, 554)`.

| Canal | Promedio | Mínimo | Máximo |
|---|---:|---:|---:|
| Rojo | 218.97 | 0 | 255 |
| Verde | 197.51 | 0 | 255 |
| Azul | 181.75 | 0 | 255 |

El canal con el promedio más alto es el **rojo**. Al observar un solo canal se pierde la información de los otros dos canales y, por tanto, el color completo de la imagen.

![Canal rojo](resultados/canal_rojo.png)
![Canal verde](resultados/canal_verde.png)
![Canal azul](resultados/canal_azul.png)

## Escala de grises

- Dimensiones: `(554, 554)`
- Intensidad promedio: `202.13`
- Intensidad mínima: `0`
- Intensidad máxima: `255`

La matriz de grises tiene dos dimensiones porque cada píxel se representa con un solo valor de intensidad. La matriz RGB tiene tres dimensiones porque cada píxel contiene tres valores: rojo, verde y azul.

Conteo de píxeles:

- Oscuros, valor menor que 85: `31,344`
- Medios, entre 85 y 170: `61,943`
- Claros, mayores que 170: `213,629`

![Escala de grises](resultados/02_escala_grises.png)

## Modificaciones

![Cuadro rojo](resultados/03_cuadro_rojo.png)

![Sin rojo](resultados/sin_rojo.png)
![Sin verde](resultados/sin_verde.png)
![Sin azul](resultados/sin_azul.png)

- Sin rojo: disminuyen los tonos rojos y predominan verdes y azules.
- Sin verde: disminuyen los tonos verdes y la imagen tiende hacia magenta.
- Sin azul: disminuyen los tonos azules y la imagen adquiere tonos más cálidos.

## Imágenes binarias

![Umbral 80](resultados/binaria_80.png)
![Umbral 128](resultados/binaria_128.png)
![Umbral 180](resultados/binaria_180.png)

Con un umbral de 80 aparecen más píxeles blancos porque se clasifican como claros más valores. Con 128 se obtiene una separación intermedia. Con 180 aumentan los píxeles negros porque se necesita una intensidad mayor para producir blanco.

## Respuestas breves

1. Una imagen RGB se representa como una matriz `(alto, ancho, 3)`.
2. Un píxel es la unidad mínima de la imagen y representa el color de una posición.
3. Los valores de 0 a 255 indican la intensidad de cada canal; 0 es ausencia y 255 es intensidad máxima.
4. RGB usa tres canales de color; escala de grises usa un solo canal de intensidad.
5. Al cambiar los valores de la matriz se modifican directamente los píxeles de la imagen.
6. Las imágenes digitales pueden analizarse y transformarse mediante operaciones matemáticas sobre matrices.

El código utilizado está en [reporte_imagenes.py](reporte_imagenes.py).
