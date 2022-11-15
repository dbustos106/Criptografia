# pip3 install pyDes
# pip3 install opencv-python

from pyDes import des, CBC, PAD_PKCS5
import numpy as np
import base64
import cv2

# Leer el archivo de entrada
img = cv2.imread('./imagen.jpg')
height = img.shape[0]
width = img.shape[1]

# Mostrar la imagen
cv2.imshow("Imagen original", img)
cv2.waitKey(5000)

# Inicializar el algoritmo Des en modo CBC
print("Procesamiento iniciado...\n")
keyBytes = bytes('secreted', 'utf-8')
algDes = des(key=keyBytes, mode=CBC, IV=b'\0\0\0\0\0\0\0\0', pad=None, padmode=PAD_PKCS5)

# Encriptar la imagen mediante el algoritmo Des
encryptedImg = algDes.encrypt(bytes(img))

# Codificar y decodificar en base64 
base64EncodedEncryptedImg = base64.b64encode(encryptedImg)
print("Texto en Base64: ", base64EncodedEncryptedImg)
base64DecodedEncryptedImg = base64.b64decode(base64EncodedEncryptedImg)

# Desencriptar la imagen mediante el algoritmo Des
decryptedImg = algDes.decrypt(base64DecodedEncryptedImg)

# Generar imagen original y mostrar
processedImg = np.frombuffer(decryptedImg, np.uint8).reshape(height, width, 3)

# Mostrar la imagen procesada
cv2.imshow("Imagen procesada", processedImg)
cv2.waitKey(5000)
cv2.destroyAllWindows()
