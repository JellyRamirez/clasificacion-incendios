import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt

#Añadir la imagen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

#Separar en canales RGB
image = cv2.imread(args["image"])
rgb_type = int(args["type"])
(B, G, R) = cv2.split(image)

#Cálculo de media/promedio
R_mean = np.average(R)
G_mean = np.average(G)
B_mean = np.average(B)

#Cálculo de desviación estandar
R_desv = np.std(R)
G_dev = np.std(G)
B_desv = np.std(B)

#Cálculo de Oblicuidad




#Cálculo de moda


