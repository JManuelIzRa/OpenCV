# encoding: utf-8
import argparse
import cv2

#Creamos la estructura que parsea los argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="751888.jpg", help="path to the input image")
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

#Acceder al pixel (x=50,y=20) y cambiarlo a rojo
image[20,50] = (0, 0, 255) # Estandar BGR

(b, g, r) = image[20,50]

print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

#Calcular el centro de la imagen, altura y ancho dividido por dos
(cX, cY) = (w // 2, h //2)

#Al ser NumPy arrays podemos usar la herramienta de array slicing para coger regiones de a imagen. Por ejemplo la parte superior izquierda de la imagen
tl = image[0:cY, 0:cX]
cv2.imshow("Esquina superior izquierda", tl)
cv2.waitKey(0)

 