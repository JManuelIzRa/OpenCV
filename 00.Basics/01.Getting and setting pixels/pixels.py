# encoding: utf-8
import argparse
import cv2

#Creamos la estructura que parsea los argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True, type=str, default="751888.jpg", help="path para añadir una imagen")
args = ap.parse_args()

#Cargamos la imagen desde el disk
#La imagen a cargar se recoge usando args["image"] si usamos vars(ap.parse_args()), si no usamos args.image
image = cv2.imread(args.image)

#Obtenemos las dimensiones de la imagen, altura y anchura
# w x h; columnas x filas
(h, w) = image.shape[:2]

cv2.imshow("OriginalImage", image)
cv2.waitKey(0)#Si no se pone se abre y se cierra instantaneamente

####################-NUEVO-#########################

#Las imagenes son NumPy arrays, con el origen (0,0) en la esquina superior izquierda
#Actualmente el estandar es RGB, pero cunado OpenCV fue desarrollado el estandar era BGR
# image[y, x] 
(b, g, r) = image[0,0]

print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
