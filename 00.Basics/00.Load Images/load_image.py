# encoding: utf-8
#Siempre que vayamos a trabajar con OpenCV, sea para lo que sea, tenemos que cargar antes en memoria las imagenes a procesar

#USO:
#python load_image.py --image something.jpg
#Para procesar los parámetros pasados por argumento
import argparse

#Para el procesamiento de imagenes
import cv2

#Creamos la estructura que parsea los argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path para añadir una imagen")
args = vars(ap.parse_args())

#Cargamos la imagen desde el disk
#La imagen a cargar se recoge usando args["image"]
image = cv2.imread(args["image"])

#Obtenemos las dimensiones de la imagen, altura, anchura y número de canales
# w x h; filas x columnas
(h, w, c) = image.shape[:3]

#Imprimir el ancho, alto y número de canales de la foto
print("Width: {} pixels".format(w))
print("Height: {} pixels".format(h))
print("Channels: {} pixels".format(c))

#Muestra la imagen y espera la pulsación de una tecla
cv2.imshow("Image", image)
cv2.waitKey(0)