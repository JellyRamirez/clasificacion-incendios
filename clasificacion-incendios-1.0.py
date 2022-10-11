import cv2
import numpy as np
import argparse

#Carga imagen normal y máscara
ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required = True, help = "Path to the original image")
ap.add_argument(("-i2", "--image2", required = True, help = "Path to the mask image")
args = vars(ap.parse_args())

image = cv2.imread(args[image1])
mask = cv2.imread(args[image2])

#Poner en forma de la máscara la imagen original
result = cv2.bitwise_and(image, mask)
# Ponemos el fondo blanco
#result[mask==0] = 255 # Optional

cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()