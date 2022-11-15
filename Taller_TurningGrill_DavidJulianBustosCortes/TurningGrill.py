import numpy as np


'''
  Está función crea la matriz de hoyos basandose
  en la ubicación suministrada por el usuario.
'''
def holeMatrix(holes, tam):
  matrix_k = np.zeros((tam, tam))
  for hole in holes:
    matrix_k[hole[0, 0], hole[0, 1]] = 1
  return matrix_k


'''
  Está función convierte un mensaje de texto en una
  matriz cuadrada.
'''
def convertToMatrix(message, tam):
  matrix_message = np.array(list(message))
  matrix_message = matrix_message.reshape((tam, tam))
  return matrix_message


'''
  Esta función encripta al mensaje m.
'''
def encrypt(m, matrix_k, tam, dirRot):
  pos = 0
  c = np.chararray((tam, tam))
  for rot in range(4):
    # Recorrer la matriz k
    for i in range(tam):
      for j in range(tam):
        if matrix_k[i, j] == 1:
          c[i, j] = m[pos]
          pos += 1

    # Si tam es impar, quitar el hoyo central
    if tam % 2 != 0:
      matrix_k[int(tam/2), int(tam/2)] = 0

    # Rotar matrix
    matrix_k = np.rot90(matrix_k, dirRot)
  
  return c


'''
  Está función imprime el mensaje cifrado c
'''
def printCipherMatrix(matrix_c, tam):
  for i in range(tam):
    for j in range(tam):
      print(matrix_c[i][j].decode("utf-8"), end="")
    print(" ", end="")


'''
  Está función desencripta al mensaje c.
'''
def decrypt(matrix_c, matrix_k, tam, dirRot):
  m = ""
  for rot in range(4):
    # Recorrer la matriz k
    for i in range(tam):
      for j in range(tam):
        if matrix_k[i, j] == 1:
          m += matrix_c[i, j]

    # Si tam es impar, quitar el hoyo central
    if tam % 2 != 0:
      matrix_k[int(tam/2), int(tam/2)] = 0

    # Rotar matrix
    matrix_k = np.rot90(matrix_k, dirRot)
    
  return m


if __name__ == '__main__':

  opcion = input("Ingrese 1 para encriptar y 0 para desencriptar:\n>> ")

  if opcion == "1":

    # Solicitar el tamaño de la retícula al usuario
    tam = input("\nIngrese el tamaño de la retícula:\n>> ")
    tam = int(tam)

    # Solicitar la dirección de rotación al usuario
    dirRot = input("\nIngrese 1 para rotar hacía la izquierda y -1 para rotar hacía la derecha:\n>> ")
    dirRot = int(dirRot)

    # Solicitar el mensaje en texto plano al usuario (plaintext)
    m = input("\nIngrese el mensaje que desea encriptar:\n>> ").lower()
    m = m.replace(" ", "")

    # Solicitar la ubicación de los hoyos (keyword)
    holes = input("\nIngrese la ubicación de los hoyos de la siguiente manera 'y1 x1; y2 x2; ...; yn xn':\n>> ").lower()
    holes = np.matrix(holes)
 
    # Crear la matriz de hoyos
    matrix_k = holeMatrix(holes, tam)
    print("\nMatriz de hoyos utilizada para cifrar:\n", matrix_k)

    print("\nEncriptación:\n")

    # Encriptar el mensaje
    matrix_c = encrypt(m, matrix_k, tam, dirRot)  

    # Imprimir el ciphertext
    print("\nCiphertext:\n")
    printCipherMatrix(matrix_c, tam)

  else: 

    # Solicitar el tamaño de la retícula al usuario
    tam = input("\nIngrese el tamaño de la retícula:\n>> ")
    tam = int(tam)

    # Solicitar la dirección de rotación al usuario
    dirRot = input("\nIngrese 1 para rotar hacía la izquierda y -1 para rotar hacía la derecha:\n>> ")
    dirRot = int(dirRot)

    # Solicitar el mensaje cifrado al usuario (ciphertext)
    c = input("\nIngrese el mensaje que desea desencriptar:\n>> ").lower()
    c = c.replace(" ", "")

    # Solicitar la ubicación de los hoyos (keyword)
    holes = input("\nIngrese la ubicación de los hoyos de la siguiente manera 'y1 x1; y2 x2; ...; yn xn':\n>> ").lower()
    holes = np.matrix(holes)

    # Crear la matriz de hoyos
    matrix_k = holeMatrix(holes, tam)
    print("\nMatriz de hoyos utilizada para cifrar:\n", matrix_k)

    print("\nDesencriptación:")

    # Convertir en matriz al mensaje cifrado c
    matrix_c = convertToMatrix(c, tam)

    # Desencriptar el mensaje
    m = decrypt(matrix_c, matrix_k, tam, dirRot)  

    # Imprimir el ciphertext 
    print("\nPlaintext:\n", m)


# Ejemplo
# thisisamessagethatiamencryptingwithaturninggrilletoprovidethisillustrativeexample
# TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE I
# 0 0; 0 3; 0 5; 1 2; 1 8; 2 1; 2 6; 3 2; 3 4; 3 7; 4 4; 4 6; 4 8; 5 3; 5 7; 6 0; 6 5; 7 1; 7 4; 7 8; 8 2

# The model of creation of images stable diffusion has given that talk during the last two weeks wow
# tnmhgehta agmhseego sdliasetv selaontfb tlhtcerwe oadatwtti ieaefoflk knsuosdwf oiiuorwni
# 0 0; 0 3; 0 5; 1 2; 1 8; 2 1; 2 6; 3 2; 3 4; 3 7; 4 4; 4 6; 4 8; 5 3; 5 7; 6 0; 6 5; 7 1; 7 4; 7 8; 8 2

# JIM ATTACKS AT DAWN
# jktd saat wiam cnat
# 0 0; 2 1; 2 3; 3 2