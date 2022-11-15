# pip3 install pyAes
# pip3 install opencv-python

from pyaes import AESModeOfOperationCBC, Encrypter, Decrypter
import numpy as np
import base64
import cv2
import os

# Solicitar al usuario el nivel de seguridad del algoritmo
seguridad = input("\nIngrese el nivel de seguridad del algoritmo (128, 192, 256):\n >> ")
seguridad = int(seguridad)

# Leer el archivo de entrada
img = cv2.imread('./imagen.jpg')
height = img.shape[0]
width = img.shape[1]

# Mostrar la imagen
cv2.imshow("Imagen original", img)
cv2.waitKey(5000)

# Inicializar el algoritmo Aes en modo CTR
print("\nProcesamiento iniciado...\n")
keyBytes = os.urandom(int(seguridad/8))
algAes = AESModeOfOperationCBC(key=keyBytes, iv=b'\0' * 16)

# Encriptar la imagen mediante el algoritmo Aes
encrypter = Encrypter(algAes)
encryptedImg = encrypter.feed(bytes(img))
encryptedImg += encrypter.feed()

# Codificar y decodificar en base64 
base64EncodedEncryptedImg = base64.b64encode(encryptedImg)
print("Texto en Base64: ", base64EncodedEncryptedImg)
base64DecodedEncryptedImg = base64.b64decode(base64EncodedEncryptedImg)

# Desencriptar la imagen mediante el algoritmo Aes
decrypter = Decrypter(algAes)
decryptedImg = decrypter.feed(base64DecodedEncryptedImg)
decryptedImg += decrypter.feed()

# Generar imagen original y mostrar
processedImg = np.frombuffer(decryptedImg, np.uint8).reshape(height, width, 3)

# Mostrar la imagen procesada
cv2.imshow("Imagen procesada", processedImg)
cv2.waitKey(5000)
cv2.destroyAllWindows()
